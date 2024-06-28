from dotenv import load_dotenv
from transformers import pipeline
import openai
import os
from llama_index.core import SimpleDirectoryReader, KnowledgeGraphIndex, ServiceContext, StorageContext
from llama_index.llms.openai import OpenAI

def load_environment_variables():
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        raise ValueError("OpenAI API key not found. Please set it in the .env file.")

def initialize_triplet_extractor():
    try:
        return pipeline('text2text-generation', model='Babelscape/rebel-large', tokenizer='Babelscape/rebel-large')
    except Exception as e:
        raise RuntimeError("Failed to initialize triplet extractor: " + str(e))

def extract_triplets(input_text, triplet_extractor):
    try:
        text = triplet_extractor.tokenizer.batch_decode([triplet_extractor(input_text, return_tensors=True, return_text=False)[0]["generated_token_ids"]])[0]
    except Exception as e:
        raise RuntimeError("Failed to extract triplets: " + str(e))

    triplets = []
    relation, subject, object_ = '', '', ''
    text = text.strip()
    current = 'x'
    for token in text.replace("<s>", "").replace("<pad>", "").replace("</s>", "").split():
        if token == "<triplet>":
            current = 't'
            if relation:
                triplets.append({'head': subject.strip(), 'type': relation.strip(), 'tail': object_.strip()})
                relation = ''
            subject = ''
        elif token == "<subj>":
            current = 's'
            if relation:
                triplets.append({'head': subject.strip(), 'type': relation.strip(), 'tail': object_.strip()})
            object_ = ''
        elif token == "<obj>":
            current = 'o'
            relation = ''
        else:
            if current == 't':
                subject += ' ' + token
            elif current == 's':
                object_ += ' ' + token
            elif current == 'o':
                relation += ' ' + token
    if subject and relation and object_:
        triplets.append((subject.strip(), relation.strip(), object_.strip()))

    return triplets

def load_documents(file_path):
    try:
        return SimpleDirectoryReader(input_files=[file_path]).load_data()
    except Exception as e:
        raise RuntimeError("Failed to load documents: " + str(e))

def create_knowledge_graph_index(documents, triplet_extractor):
    service_context = ServiceContext.from_defaults(llm=OpenAI(model_name="gpt-3.5-turbo"), chunk_size=256)
    return KnowledgeGraphIndex.from_documents(documents, kg_triplet_extract_fn=lambda x: extract_triplets(x, triplet_extractor), service_context=service_context)

def save_index(index, file_path):
    try:
        index.storage_context.persist(persist_dir=file_path)
    except Exception as e:
        raise RuntimeError("Failed to save index: " + str(e))

def query_index(index, query):
    try:
        response = index.as_query_engine().query(query)
        print(response)
    except Exception as e:
        raise RuntimeError("Failed to query index: " + str(e))

def main():
    try:
        load_environment_variables()
        triplet_extractor = initialize_triplet_extractor()
        documents = load_documents("./paul_graham_essay.txt")
        index = create_knowledge_graph_index(documents, triplet_extractor)
        save_index(index, "./")

        queries = ["What happened to the author after YC?", "What happened to the author at Interleaf?"]
        for query in queries:
            query_index(index, query)
    except Exception as e:
        print("An error occurred: " + str(e))

if __name__ == "__main__":
    main()
