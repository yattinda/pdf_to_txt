from pypdf import PdfReader
from app.func.parser_pdf import textParser


def to_txt(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
        text += " "
    text = textParser(text)

    return text
