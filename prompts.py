from langchain_core.prompts import ChatPromptTemplate


DIFFICULTY_INSTRUCTIONS = {

    "Beginner": """
Use simple language.

Requirements:
- Explain concepts from the basics.
- Avoid unnecessary technical jargon.
- Use simple examples.
- MCQs should test fundamental understanding.
- Short answers should be easy to understand.
""",

    "Intermediate": """
Use moderate technical depth.

Requirements:
- Assume the student understands basic terminology.
- Include conceptual relationships.
- Include practical examples.
- MCQs should test understanding and application.
- Short answers should require explanation.
""",

    "Advanced": """
Use advanced technical depth.

Requirements:
- Assume strong foundational knowledge.
- Use appropriate technical terminology.
- Test analysis, comparison and application.
- Include challenging MCQ distractors.
- Short answers should require deeper reasoning.
"""
}


STUDY_GUIDE_PROMPT = ChatPromptTemplate.from_messages(
    [

        (
            "system",
            """
You are an expert university study-guide generator.

Create a complete study pack using ONLY the
educational content provided by the user.

IMPORTANT REQUIREMENTS:

1. Generate exactly 20 MCQs.
2. Generate exactly 5 short-answer questions.
3. Every MCQ must have exactly four options.
4. Every MCQ must have one correct answer.
5. Every MCQ must include an explanation.
6. Generate a useful glossary.
7. Generate a logical study order.
8. Do not invent unsupported facts.
9. Follow the selected difficulty level.
10. Return the response according to the
    requested structured schema.

Difficulty instructions:

{difficulty_instructions}
"""
        ),

        (
            "human",
            """
Create the complete study pack from the
following lecture/syllabus content:

{content}
"""
        )

    ]
)