"""
API specific models and routes for RAG.
"""
from fastapi import APIRouter

rag_router = APIRouter()

@rag_router.get("/status")
def status():
    """RAG pipeline status."""
    return {"status": "operational"}
