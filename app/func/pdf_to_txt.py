from pypdf import PdfReader

def to_txt(file):
    reader = PdfReader(file)
    text = ""

    for page in reader.pages:
        text += page.extract_text() 
        text += " "

    return text
