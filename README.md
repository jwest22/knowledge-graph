### Overview

This project uses a combination of OpenAI and Babelscape's rebel-large model to extract subject-relation-object triplets from text. The script processes the text, identifies relational triplets, and accepts user text queries regarding the content of the constructed knowledge graph. 

#### Setup

1. Environment Setup:
   - Ensure you have the necessary API keys and libraries installed.
   - Set the OPENAI_API_KEY environment variable with your OpenAI API key.

2. Install Dependencies:
   pip install transformers openai llama_index

#### Usage

1. Triplet Extraction:
   - The extract_triplets function extracts subject-relation-object triplets from the input text using the rebel-large model.

2. Document Loading:
   - Load documents using SimpleDirectoryReader.

3. Service Context:
   - Configure the service context with OpenAI's gpt-3.5-turbo model.

4. Knowledge Graph Index:
   - Create a knowledge graph index from the loaded documents.
   - Extract triplets using the extract_triplets function.

5. Querying:
   - Query the knowledge graph for specific information.

6. Visualization:
   - Generate and display a network graph of the extracted triplets.

#### Example Queries

**Q:** "What happened to the author after YC?"
**A:** "The author's life after YC remains undisclosed or unspecified."

**Q:** "What happened to the author at Interleaf?"
**A:** "The author did not establish any relationships at Interleaf."

#### Notes

- Ensure that the paul_graham_essay.txt file is present in the specified directory.
- The script supports chunk sizes up to 512 for processing.
