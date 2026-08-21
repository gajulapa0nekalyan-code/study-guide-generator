import os
import json

from dotenv import load_dotenv
from groq import Groq

from models import StudyPack


# ------------------------------------------------
# Load Environment Variables
# ------------------------------------------------

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY not found. Check your .env file."
    )


# ------------------------------------------------
# Groq Client
# ------------------------------------------------

client = Groq(
    api_key=GROQ_API_KEY
)


# ------------------------------------------------
# Generate Study Pack
# ------------------------------------------------

def generate_study_pack(content, difficulty="beginner"):
    """
    Generate a structured study pack using Groq.
    """

    prompt = f"""
You are an expert educational AI assistant.

Create a complete study pack from the study material below.

Difficulty level:
{difficulty}

Study material:
{content}

Generate:

1. SUMMARY NOTES
2. EXACTLY 20 MULTIPLE CHOICE QUESTIONS
3. EXACTLY 5 SHORT-ANSWER QUESTIONS
4. KEY TERMS GLOSSARY
5. SUGGESTED STUDY ORDER

Difficulty rules:

Beginner:
- Simple explanations
- Basic terminology
- Easy questions

Intermediate:
- Moderate explanations
- Conceptual questions
- Moderate difficulty

Advanced:
- Detailed explanations
- Application-based questions
- Challenging questions

For every MCQ provide:

- question
- option_a
- option_b
- option_c
- option_d
- correct_answer
- explanation

The correct_answer must be only:
A, B, C, or D.

For every short-answer question provide:

- question
- model_answer

For glossary items provide:

- term
- definition

For study order provide:

- step_number
- topic
- reason

IMPORTANT:

Return ONLY valid JSON.

Do not use markdown.
Do not use ```json.
Do not add any text outside the JSON.

Use this exact structure:

{{
    "title": "Study Guide Title",

    "summary_notes": "Summary of the study material",

    "mcqs": [
        {{
            "question": "Question text",
            "option_a": "Option A",
            "option_b": "Option B",
            "option_c": "Option C",
            "option_d": "Option D",
            "correct_answer": "A",
            "explanation": "Explanation"
        }}
    ],

    "short_answers": [
        {{
            "question": "Question text",
            "model_answer": "Model answer"
        }}
    ],

    "glossary": [
        {{
            "term": "Term",
            "definition": "Definition"
        }}
    ],

    "study_order": [
        {{
            "step_number": 1,
            "topic": "Topic",
            "reason": "Reason"
        }}
    ]
}}

Rules:

- Exactly 20 MCQs
- Exactly 5 short-answer questions
- Provide useful glossary terms
- Provide a logical study order
- Keep the content based on the supplied study material
"""


    # ------------------------------------------------
    # Groq API Call
    # ------------------------------------------------

    response = client.chat.completions.create(

        model="openai/gpt-oss-20b",

        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert educational "
                    "AI assistant. Return valid JSON only."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.3,

        max_tokens=5000,

        response_format={
            "type": "json_object"
        }
    )


    # ------------------------------------------------
    # Get AI Response
    # ------------------------------------------------

    result = response.choices[0].message.content


    # ------------------------------------------------
    # Convert JSON String to Python Dictionary
    # ------------------------------------------------

    try:

        data = json.loads(result)

    except json.JSONDecodeError as error:

        raise ValueError(
            f"Groq returned invalid JSON: {error}"
        )


    # ------------------------------------------------
    # Convert Dictionary to StudyPack
    # ------------------------------------------------

    try:

        study_pack = StudyPack.model_validate(data)

    except Exception as error:

        raise ValueError(
            f"Invalid study pack structure: {error}"
        )


    # ------------------------------------------------
    # Return Structured Object
    # ------------------------------------------------

    return study_pack