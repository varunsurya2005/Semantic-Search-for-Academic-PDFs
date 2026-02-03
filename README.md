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

## System Design (Current)
  PDFs

   ↓

Text Extraction


↓

Chunking

↓

Embeddings (SentenceTransformers)

↓

Endee Vector Index

↓

Semantic Similarity Search
### Tech Stack

Python 3

SentenceTransformers (all-MiniLM-L6-v2)

Endee Vector Database

PyPDF

Docker (for Endee server)

### How Endee Is Used

Stores dense vector embeddings of PDF text chunks

Performs cosine similarity search

Returns ranked, semantically relevant passages

Acts as the retrieval backbone for future RAG pipelines

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

## Screenshot of working example
<img width="589" height="253" alt="{F4CAD278-A1D0-4D65-B6C8-5C058E0CB09A}" src="https://github.com/user-attachments/assets/6fae274a-04bd-4ebb-9ee9-ebc578cd8c5b" />
