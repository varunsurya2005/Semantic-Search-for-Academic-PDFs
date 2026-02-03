import os
from endee import Endee, Precision
from embeddings import generate_embedding
from pdf_loader import extract_text_from_pdf
from chunker import chunk_text

INDEX_NAME = "semantic_docs"
VECTOR_DIM = 384
PDF_DIR = "data/pdfs"


def ingest():
    client = Endee()

    # ---- create index if needed ----
    try:
        client.create_index(
            name=INDEX_NAME,
            dimension=VECTOR_DIM,
            space_type="cosine",
            precision=Precision.INT8D
        )
        print("✅ Created Endee index")
    except Exception:
        print("ℹ️ Index already exists")

    index = client.get_index(INDEX_NAME)

    # ---- load PDFs ----
    print("📂 PDFs found:", os.listdir(PDF_DIR))

    documents = []
    for file in os.listdir(PDF_DIR):
        if file.endswith(".pdf"):
            pdf_path = os.path.join(PDF_DIR, file)
            pages = extract_text_from_pdf(pdf_path)
            print(f"📄 Pages extracted from {file}: {len(pages)}")

            for page in pages:
                documents.extend(chunk_text(page))

    print("🧩 Total chunks:", len(documents))

    # ---- embeddings ----
    vectors = []
    skipped = 0

    for i, text in enumerate(documents):
        embedding = generate_embedding(text)
        if embedding is None:
            skipped += 1
            continue

        vectors.append({
            "id": f"chunk_{i}",
            "vector": embedding,
            "meta": {"text": text}
        })

    print("🧠 Vectors to insert:", len(vectors))
    print("⏭️ Skipped chunks:", skipped)

    if vectors:
        index.upsert(vectors)
        print(f"✅ Ingested {len(vectors)} vectors into Endee")
    else:
        print("❌ No vectors generated — ingestion failed")


if __name__ == "__main__":
    ingest()
