
"""
Here, we implement a functuion using the transformers pipeline to
get a list of keywords relevant to the role that are required or useful skills.
"""

"""
Going to try out using yake for keyword compilation, as gpt2
went to the bar this weekend.
"""

import yake

# defining the kw function (20 is the number of most similar keywords to return.)

def generate_keywords_from_resume(text, top_n=20):
    # using yake's keywordExtractor function to get english keywords that consist of one word (n) and 20 most relevant ones.
    kw_extractor = yake.KeywordExtractor(lan="en", n=1, top=top_n)
    # get a list of tuples containing each of the 20 top keywords and their own individual similarity score.
    keywords_with_scores = kw_extractor.extract_keywords(text)
    # collecting the keywords without the scores. We only care about the kwywords not necessarily their rank.
    keywords = [kw for kw, score in keywords_with_scores]
