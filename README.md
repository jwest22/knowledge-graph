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

**A:** "The author decided to hand over YC to someone else after his mother had a stroke and he realized he was ready to make a change. He asked Jessica if she wanted to be president, but she declined. They then decided to recruit Sam Altman to take over. Eventually, Sam agreed to become the president of YC, leading to a complete changing of the guard. The author and another founder retired, while Jessica and another partner became ordinary partners."

**Q:** "What happened to the author at Interleaf?"

**A:** "The author was determined to be the Microsoft Word, not the Interleaf."

#### Notes

- Ensure that the paul_graham_essay.txt file is present in the specified directory.
- The script supports chunk sizes up to 512 for processing.
