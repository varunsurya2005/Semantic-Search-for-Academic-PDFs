def chunk_text(text, chunk_size=300, overlap=50):
    if not isinstance(text, str):
        return []

    words = text.split()
    chunks = []

    start = 0
    while start < len(words):
        end = start + chunk_size
        chunk = " ".join(words[start:end]).strip()
        if chunk:
            chunks.append(chunk)
        start = end - overlap

    return chunks
