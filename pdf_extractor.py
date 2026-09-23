from pypdf import PdfReader

def extract_pdf_text(path):
    reader = PdfReader(path)
    pages = []
    for i, page in enumerate(reader.pages):
        pages.append({"text": page.extract_text(), "page": i + 1})
    return pages

path= "pdf\Technologies des services.pdf"

pages= extract_pdf_text(path)
print(pages)