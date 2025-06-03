import os
from dotenv import load_dotenv
import os
from dotenv import load_dotenv
from resume_parser import extract_text_from_pdf

"""
Note: keyword_generator is a .py file we create in which there exists a function
generate_keywords_for_biotech_ds_role().

"""
#from keyword_generator import generate_keywords_for_biotech_ds_role

# Load API key from .env
load_dotenv()
OPENAI_API_KEY = os.getenv("XXX")

# Path to PDF resume
resume_path = "sample_resumes/candidate1.pdf"

# Step 1: Extract text from PDF
resume_text = extract_text_from_pdf(resume_path)
