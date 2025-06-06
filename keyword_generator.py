
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
generator = pipeline("text-generation", model="gpt2")

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


# Note: this was the first response!!!
#
# Device set to use cpu
# Truncation was not explicitly activated but `max_length` is provided a specific value, please use `truncation=True` to explicitly truncate examples to max length. Defaulting to 'longest_first' truncation strategy. If you encode pairs of sequences (GLUE-style) with the tokenizer you can select this strategy more precisely by providing a specific strategy to `truncation`.
# Setting `pad_token_id` to `eos_token_id`:50256 for open-end generation.
# List 15 key technical skills for a Data Scientist in Biotechnology. Read more.
#
# Q. What's the key to becoming a good Data Scientist?
#
# A. The Key is to Be Responsive. Responsiveness is in control. The world of business has changed. The focus has changed. This is what has changed. Every business has changed. The Data Science field is about getting people to use the data.
#
# Q. I can't stay on my team in our organization for
#
# Process finished with exit code 0
