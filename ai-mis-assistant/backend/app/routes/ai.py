from pydantic import BaseModel, Field
from fastapi import APIRouter
from app.ai.agent import respond

router = APIRouter()


class Question(BaseModel):
    question: str = Field(min_length=2, max_length=1000)


@router.post("/ask")
def ask(body: Question):
    return respond(body.question)
