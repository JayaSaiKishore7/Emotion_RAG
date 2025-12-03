"""
Minimal stub for core.models so app.py can import while you restore full file.
Replace with your full implementation later.
"""
import time

def load_emotion_model():
    # returns (processor, model, device)
    # stub: return None placeholders and "cpu"
    return None, None, "cpu"

def predict_emotion(processor, model, device, image):
    # stub: return a predictable emotion
    return "neutral"

def load_rag_pipeline():
    # returns (db, llm, embeddings, sentiment_pipe, sentiment_labels)
    return None, None, None, None, None

def query_rag(qa_chain, query):
    # Return a fake RAG response to let the UI proceed
    return {"result": "No RAG index available (stub).", "source_documents": []}

def analyze_sentiment(pipe, labels, text):
    return "NEUTRAL (Score: 0.00)"
