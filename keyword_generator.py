
"""
Here, we will write code to use openai's relevant API to get relevant
keywords using a prompt that is designed to ask for specific keywords for
a bio-meets-datascience role. Kind of exxcited to see what it'lll
return!
"""

import openai

def generate_keywords_for_biotech_ds_role(api_key):
    openai.api_key = api_key

    prompt = """
We are a biotechnology company looking to hire someone at the intersection of Bioinformatics and Data Science.

List 20 must-have skills or keywords you expect to see in a strong candidate's resume. Include a mix of:
- Bio data analysis
- Machine learning or AI
- Genetic sequence analysis
- Python libraries
- Lab data handling

Return it as a plain Python list of strings.
"""
