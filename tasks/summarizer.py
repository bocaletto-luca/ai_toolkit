# tasks/summarizer.py
from transformers import pipeline

_summarizer = pipeline("summarization", model="t5-small")

def summarize(text: str, max_length: int = 150) -> str:
    res = _summarizer(
        text, max_length=max_length, min_length=30, do_sample=False
    )
    return res[0]["summary_text"]
