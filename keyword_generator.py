
"""
Here, we will write code to use openai's relevant API to get relevant
keywords using a prompt that is designed to ask for specific keywords for
a bio-meets-datascience role. Kind of exxcited to see what it'lll
return!

Openai's chat API requires two things:

1. role - tells the API what the response should sound like its from.
2. content - the prompt
"""

import openai

def generate_keywords_for_biotech_ds_role(api_key):
    openai.api_key = """some secret key which you will neeeeever knoooow"""

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


    """
    Note: 'temperature' in this sense refers to how much 'creativity' or 'randomness' is 
    required in the output.
    
    0.0 would be safe and boring.
    1.0 would be a comedian / artist on steroids
    
    So we chosose the average 0.5
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # the free-tier
        messages=[
            {"role": "system", "content": "You are a helpful AI recruiter assistant."},
            {"role": "user", "content": prompt}   # this prompt is written above.
        ],
        temperature=0.5
    )

