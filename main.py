from pdf_extractor import extract_pdf_text
from chunker import chunk_text

path= "pdf\Technologies des services.pdf"

pages= extract_pdf_text(path)
chunks = [chunk_text(page["text"]) for page in pages]
print(chunks)