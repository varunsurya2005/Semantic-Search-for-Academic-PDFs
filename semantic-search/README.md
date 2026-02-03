# Semantic Search Service (Retrieval Layer)
## Purpose

This module implements the retrieval layer of a larger exam-preparation platform.
It is responsible for ingesting PDFs, generating embeddings, storing vectors in Endee, and performing semantic similarity search.

####  folder does not include:

1) Web UI

2) User authentication

3) Answer generation (RAG)

4) Those are planned as future components.

#### What This Module Does

1) Extracts text from academic PDFs

2) Chunks content into semantically meaningful units
3) Generates dense embeddings using SentenceTransformers
4) Indexes embeddings in Endee

### Retrieves relevant text passages for a given query

<img width="330" height="222" alt="{D40EC16E-A971-4EDA-A52E-CA0720E6768F}" src="https://github.com/user-attachments/assets/e323d3fd-52dd-48f6-971c-7d5b0175e3a0" />


### Processing Pipeline

<img width="216" height="210" alt="{D0E06EF2-2C9C-4715-A517-C1742F21F7DC}" src="https://github.com/user-attachments/assets/d895cea5-c5f4-4ce0-b92f-bbceb0090872" />



## Setup Instructions
1. ### Start Endee Server

docker compose up -d

2. ### Install Dependencies
py -m pip install -r requirements.txt

3. ### Ingest PDFs

Place PDF files in:  data/pdfs/


4) ### Then run:

py src/ingest.py

5) ### Running Semantic Search
py src/search.py


## Output

Returns top-k semantically similar chunks

Displays similarity scores

Results are ranked by cosine similarity

## Design Notes

Retrieval is semantic, not keyword-based

Mixed-topic PDFs may return related concepts

Input validation prevents tokenizer failures

Code is modular to support future RAG integration

## Future Extensions (Not Implemented Here)

RAG (LLM-based answer generation)

Metadata filtering (subject, unit, exam type)

OCR for scanned PDFs

API endpoints for web integration
