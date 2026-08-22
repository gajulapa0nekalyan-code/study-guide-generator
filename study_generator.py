import os
import json

from dotenv import load_dotenv
from groq import Groq

from models import StudyPack


# ------------------------------------------------
# Load Environment Variables
# ------------------------------------------------

load_dotenv()


# ------------------------------------------------
# Get Groq API Key
# ------------------------------------------------

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Streamlit Cloud Secrets
if not GROQ_API_KEY:
    try:
        import streamlit as st
        GROQ_API_KEY = st.secrets.get("GROQ_API_KEY")
    except Exception:
        GROQ_API_KEY = None


if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY not found. "
        "Add GROQ_API_KEY to Streamlit Cloud Secrets."
    )


# ------------------------------------------------
# Get Groq Model
# ------------------------------------------------

GROQ_MODEL = os.getenv("GROQ_MODEL")

if not GROQ_MODEL:
    try:
        import streamlit as st
        GROQ_MODEL = st.secrets.get("GROQ_MODEL")
    except Exception:
        GROQ_MODEL = None


if not GROQ_MODEL:
    GROQ_MODEL = "openai/gpt-oss-20b"


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
- Beginner-friendly examples

Intermediate:
- Moderate explanations
- Conceptual questions
- Moderate difficulty
- Practical examples

Advanced:
- Detailed explanations
- Application-based questions
- Challenging questions
- Deeper technical reasoning

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
- Keep content based on the supplied study material
- Difficulty must measurably affect output complexity
"""

    # ------------------------------------------------
    # Groq API Call
    # ------------------------------------------------

    response = client.chat.completions.create(
        model=GROQ_MODEL,

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
    # Convert JSON String
    # ------------------------------------------------

    try:
        data = json.loads(result)

    except json.JSONDecodeError as error:

        raise ValueError(
            f"Groq returned invalid JSON: {error}"
        )

    # ------------------------------------------------
    # Validate Study Pack
    # ------------------------------------------------

    try:
        study_pack = StudyPack.model_validate(data)

    except Exception as error:

        raise ValueError(
            f"Invalid study pack structure: {error}"
        )

    return study_pack