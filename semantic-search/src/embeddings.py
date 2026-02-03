from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_embedding(text):
    if text is None:
        return None

    if not isinstance(text, str):
        try:
            text = str(text)
        except Exception:
            return None

    text = text.strip()

    if len(text) == 0:
        return None

    try:
        return model.encode(text).tolist()
    except Exception:
        
        return None
