from pypdf import PdfReader

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    pages_text = []

    for page in reader.pages:
        text = page.extract_text()
        if text and isinstance(text, str):
            clean = text.strip()
            if clean:
                pages_text.append(clean)

    return pages_text
