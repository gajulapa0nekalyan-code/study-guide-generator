import streamlit as st

from pdf_processor import extract_pdf_text
from study_generator import generate_study_pack

from exporters import create_pdf, create_mcq_csv


# ------------------------------------------------
# Page Configuration
# ------------------------------------------------

st.set_page_config(

    page_title=
        "AI Study Guide Generator",

    page_icon=
        "📚",

    layout=
        "wide"
)


# ------------------------------------------------
# Header
# ------------------------------------------------

st.title(
    "📚 AI Study Guide Generator"
)


st.write(

    """
Upload a lecture PDF or paste syllabus content
and generate a complete AI-powered study pack.
"""
)


# ------------------------------------------------
# Sidebar
# ------------------------------------------------

st.sidebar.header(
    "⚙️ Study Settings"
)


difficulty = st.sidebar.selectbox(

    "Select Difficulty",

    [

        "Beginner",

        "Intermediate",

        "Advanced"

    ]
)


# ------------------------------------------------
# Input Method
# ------------------------------------------------

input_method = st.radio(

    "Choose Input Method",

    [

        "Upload PDF",

        "Paste Text"

    ],

    horizontal=True
)


content = ""


# ------------------------------------------------
# PDF Input
# ------------------------------------------------

if input_method == "Upload PDF":


    uploaded_file = st.file_uploader(

        "Upload Lecture PDF",

        type=["pdf"]
    )


    if uploaded_file:


        try:


            content = extract_pdf_text(

                uploaded_file
            )


            st.success(

                "✅ PDF uploaded successfully!"
            )


            with st.expander(

                "Preview Extracted Text"
            ):


                st.text(

                    content[:5000]
                )


        except Exception as error:


            st.error(

                str(error)
            )


# ------------------------------------------------
# Text Input
# ------------------------------------------------

else:


    content = st.text_area(

        "Paste your syllabus or lecture content",

        height=300,

        placeholder=

        """
Example:

Introduction to Machine Learning

Machine Learning is a branch of Artificial
Intelligence that allows computers to learn
patterns from data...
"""
    )


# ------------------------------------------------
# Generate Button
# ------------------------------------------------

if st.button(

    "🚀 Generate Study Pack",

    type="primary"
):


    if not content.strip():


        st.warning(

            "⚠️ Please upload a PDF "
            "or paste some content."
        )


    else:


        with st.spinner(

            "🤖 Groq is generating "
            "your study pack..."
        ):


            try:


                study_pack = generate_study_pack(

                    content,

                    difficulty
                )


                # Validate MCQs

                if len(
                    study_pack.mcqs
                ) != 20:


                    raise ValueError(

                        f"Expected 20 MCQs, "
                        f"but received "
                        f"{len(study_pack.mcqs)}."
                    )


                # Validate Short Answers

                if len(
                    study_pack.short_answers
                ) != 5:


                    raise ValueError(

                        f"Expected 5 short-answer "
                        f"questions, but received "
                        f"{len(study_pack.short_answers)}."
                    )


                st.session_state[
                    "study_pack"
                ] = study_pack


                st.success(

                    "🎉 Study pack generated successfully!"
                )


            except Exception as error:


                st.error(

                    f"❌ Generation failed: {error}"
                )


# ------------------------------------------------
# Display Study Pack
# ------------------------------------------------

if "study_pack" in st.session_state:


    study_pack = st.session_state[
        "study_pack"
    ]


    st.divider()


    st.header(

        f"📖 {study_pack.title}"
    )


    # ------------------------------------------------
    # Summary
    # ------------------------------------------------

    st.subheader(

        "📝 Summary Notes"
    )


    st.write(

        study_pack.summary_notes
    )


    # ------------------------------------------------
    # MCQs
    # ------------------------------------------------

    st.subheader(

        "❓ 20 Practice MCQs"
    )


    for index, mcq in enumerate(

        study_pack.mcqs,

        start=1
    ):


        st.markdown(

            f"### {index}. "
            f"{mcq.question}"
        )


        st.write(

            f"A. {mcq.option_a}"
        )


        st.write(

            f"B. {mcq.option_b}"
        )


        st.write(

            f"C. {mcq.option_c}"
        )


        st.write(

            f"D. {mcq.option_d}"
        )


        with st.expander(

            "🔎 Show Answer & Explanation"
        ):


            st.success(

                f"Correct Answer: "
                f"{mcq.correct_answer}"
            )


            st.write(

                mcq.explanation
            )


    # ------------------------------------------------
    # Short Answers
    # ------------------------------------------------

    st.subheader(

        "✍️ 5 Short-Answer Questions"
    )


    for index, item in enumerate(

        study_pack.short_answers,

        start=1
    ):


        st.markdown(

            f"### {index}. "
            f"{item.question}"
        )


        with st.expander(

            "💡 Show Model Answer"
        ):


            st.write(

                item.model_answer
            )


    # ------------------------------------------------
    # Glossary
    # ------------------------------------------------

    st.subheader(

        "📚 Key Terms Glossary"
    )


    for item in study_pack.glossary:


        st.markdown(

            f"**{item.term}**"
        )


        st.write(

            item.definition
        )


    # ------------------------------------------------
    # Study Order
    # ------------------------------------------------

    st.subheader(

        "🗺️ Suggested Study Order"
    )


    for step in study_pack.study_order:


        st.markdown(

            f"**{step.step_number}. "
            f"{step.topic}**"
        )


        st.write(

            step.reason
        )


    # ------------------------------------------------
    # Downloads
    # ------------------------------------------------

    st.divider()


    st.header(

        "📥 Download Study Materials"
    )


    pdf_file = create_pdf(

        study_pack
    )


    csv_file = create_mcq_csv(

        study_pack
    )


    col1, col2 = st.columns(2)


    with col1:


        st.download_button(

            label=
                "📄 Download Study Pack PDF",

            data=
                pdf_file,

            file_name=
                "study_pack.pdf",

            mime=
                "application/pdf"
        )


    with col2:


        st.download_button(

            label=
                "📊 Download MCQs CSV",

            data=
                csv_file,

            file_name=
                "mcqs.csv",

            mime=
                "text/csv"
        )