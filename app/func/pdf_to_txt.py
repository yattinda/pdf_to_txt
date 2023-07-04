from pypdf import PdfReader
from app.func.parser_pdf import textParser

ALLOWED_EXTENSIONS = {"pdf"}


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def to_txt(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
        text += " "
    text = textParser(text)

    return text
