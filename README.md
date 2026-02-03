# Semantic Search Engine for Exam Preparation (Endee)
 ## Project Overview

This project implements a semantic search engine designed as a core component of a future exam-preparation platform.

The long-term vision is to support a website where teachers upload lecture notes, recent papers, and previous exam PDFs, enabling students to study using intelligent semantic search and AI assistance.

The current implementation focuses on the retrieval layer using embeddings and a vector database.

RAG and the web application will be implemented in future phases.

The system uses Endee for vector storage and similarity search.

## Problem Statement

Students often study from large collections of PDFs such as:

1) Lecture notes

2) Recent academic papers

3) Previous exam question papers

Traditional keyword search is ineffective for conceptual questions and varied terminology.

This project addresses that limitation by enabling semantic search, allowing students to retrieve relevant study material using natural-language queries.

## Current Scope (Implemented)

1) PDF text extraction

2) Chunking of academic content

3) Embedding generation using SentenceTransformers

4) Vector indexing and similarity search using Endee

5) Command-line interface (CLI) for semantic queries

6) Robust handling of noisy and mixed academic PDFs

## Planned Future Scope
### Web Application (Future)

Teachers upload PDFs via a website

Uploaded PDFs are automatically ingested

Students search through course materials online

RAG – Retrieval-Augmented Generation (Future)

Retrieved chunks passed to an LLM

System generates concise, exam-oriented answers

Answers grounded strictly in uploaded PDFs

⚠️ Note: RAG and the website are not part of the current implementation and are planned as future enhancements.

### Tech Stack

Python 3

SentenceTransformers (all-MiniLM-L6-v2)

Endee Vector Database

PyPDF

Docker (for Endee server)

### Role of Endee in the System

Endee is responsible for:

1) Storing high-dimensional vector embeddings of document text

2) Performing fast similarity search over those vectors

3) Returning the most relevant document chunks for a given user query

3) Endee acts as the retrieval layer of the AI system.

### Endee Usage Workflow (Step-by-Step)
1) #### Index Creation in Endee

An index is created in Endee to store document embeddings.

client.create_index(
    name="semantic_docs",
    dimension=384,
    space_type="cosine",
    precision=Precision.INT8D
)


dimension = 384 → matches the embedding size produced by the sentence-transformer model

cosine similarity → used for semantic similarity search

INT8D precision → optimized for memory and performance

This index is created once and reused across runs.

2) #### Ingesting Data into Endee

During ingestion:

1) PDF files are loaded

2) Each page is split into smaller text chunks

3) Each chunk is converted into a vector embedding

4) Vectors are stored in Endee along with metadata

<img width="572" height="319" alt="image" src="https://github.com/user-attachments/assets/54f46108-466f-4f68-976e-1b2a479d373c" />

vector → numerical representation of text

meta.text → original text used later for display or answer generation

meta.source/page → enables traceability to the original document

Endee stores both vectors and metadata, making retrieval contextual and explainable.

3) ### Querying Endee for Semantic Search

When a user enters a query:

The query is converted into an embedding

Endee performs similarity search

Top-K relevant document chunks are returned

<img width="380" height="161" alt="image" src="https://github.com/user-attachments/assets/a21fb19d-d536-478d-ab5c-4fa47b79a803" />

Endee returns:
The most semantically similar chunks

Metadata (original text, source, page number)

This allows the system to retrieve meaning-based results, not keyword matches.

### Why Endee Was Chosen

Endee was chosen because:

It is optimized for vector search and retrieval

It supports high-performance similarity search

It integrates easily with Python-based ML workflows

It is suitable for production-grade AI systems

This project demonstrates a real-world usage of Endee in an AI retrieval pipeline.

### System Architecture
<img width="490" height="351" alt="image" src="https://github.com/user-attachments/assets/602d354f-5261-4a62-ab2d-9ee350021ef3" />


Endee is the central component enabling efficient and scalable semantic retrieval.

## Setup & Execution
1️⃣ Start Endee Server

docker compose up -d

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Ingest PDFs

py src/ingest.py

4️⃣ Run Semantic Search

py src/search.py

### Example Queries
define data warehouse
characteristics of data warehouse
data warehouse architecture

### Example Output
Score: 0.55
Data Warehousing and Data Mining UNIT 02...

Score: 0.41
Benefits of FP-tree Structure...

## Design Decisions & Limitations

The system performs semantic retrieval, not direct question answering

Results may include conceptually related topics when PDFs contain mixed subjects

This behavior is expected in vector-based retrieval systems

Improved chunking, metadata filtering, and RAG can refine accuracy

## Use Case Alignment

This project demonstrates:

Practical use of vector databases

Embedding-based similarity search

Handling real academic PDF data

Foundations for scalable AI-powered education tools

## Future Enhancements

Full RAG pipeline for answer generation

Website integration for teachers and students

Metadata-based filtering (subject, unit, paper type)

OCR support for scanned PDFs

Performance and relevance evaluation metrics


