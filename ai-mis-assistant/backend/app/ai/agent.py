from app.ai.llm_service import answer_question
from app.ai.rag_service import search_policies


def respond(question: str) -> dict:
    policies = search_policies(question)
    return {"answer": answer_question(question), "sources": policies}
