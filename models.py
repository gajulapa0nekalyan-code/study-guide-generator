from typing import List
from pydantic import BaseModel, Field


class MCQ(BaseModel):
    question: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str
    correct_answer: str
    explanation: str


class ShortAnswer(BaseModel):
    question: str
    model_answer: str


class GlossaryTerm(BaseModel):
    term: str
    definition: str


class StudyStep(BaseModel):
    step_number: int
    topic: str
    reason: str


class StudyPack(BaseModel):
    title: str

    summary_notes: str

    mcqs: List[MCQ] = Field(
        default_factory=list,
        description="Exactly 20 multiple choice questions"
    )

    short_answers: List[ShortAnswer] = Field(
        default_factory=list,
        description="Exactly 5 short answer questions"
    )

    glossary: List[GlossaryTerm] = Field(
        default_factory=list
    )

    study_order: List[StudyStep] = Field(
        default_factory=list
    )