
"""
Here, we implement a functuion using the transformers pipeline to
get a list of keywords relevant to the role that are required or useful skills.
"""

from transformers import pipeline

"""
within the pipeline function, the "text-generation" argument simply tells the model
what we require, and the model specifies that we need the gpt2
model (small GPT-2 model with about 124M parameters):
"""
generator = pipeline("text-generation", model="sshleifer/tiny-gpt2")

"""this is what we are inputting into the model, the prompt. its asking for the relevant keywords:"""

prompt = "List 15 key technical skills for a Data Scientist in Biotechnology."

"""
asks for the output to be a minimum of 100 tokens (like 75-100 words) and
num_return_sequences = 1 simply asks the model to generate just one
response (many are possible.)
"""

response = generator(prompt, max_length=100, num_return_sequences=1)

"""
Note the 0 index isn't really necessary as its just one response.
"""

print(response[0]["generated_text"])

#
