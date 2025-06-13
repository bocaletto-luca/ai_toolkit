# tasks/qa.py
from transformers import pipeline

_qa = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

def answer(question: str, context: str) -> str:
    res = _qa(question=question, context=context)
    return res["answer"]
