import pdfplumber

"""
This is the function to get pdf text using python's promising
pdfplumber module.

As you can guess, file_path is the path to the resume to be examined.

pdfplumber sees each page as an object. using the 
page.extract() function should work (I haven't tried it yet!)
"""

def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text.lower()  # Lowercase for easier matching
