from resume_parser import extract_text_from_pdf
from keyword_generator import generate_keywords_from_resume

"""
Note: keyword_generator is a .py file we create in which there exists a function
generate_keywords_for_biotech_ds_role().

"""
def main():
    resume_path = "Elena00_resume.pdf"
    resume_text = extract_text_from_pdf(resume_path)
    print(resume_text)

main()
