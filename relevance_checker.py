
"""
This function accepts the resume's text and the keywords from the api
and splits the words into two lists:

1. matched
2. missing

the score object is simply the fraction of matching keywords from the
resume. The missing one can be thought of as "1 - matching".
"""

def check_relevance(resume_text, keywords):
    matched = [kw for kw in keywords if kw in resume_text]
    missing = [kw for kw in keywords if kw not in resume_text]
    score = len(matched) / len(keywords) if keywords else 0

    return {
        "matched": matched,
        "missing": missing,
        "score": score
    }
