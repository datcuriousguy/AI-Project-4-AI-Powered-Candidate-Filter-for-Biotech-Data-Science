
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
