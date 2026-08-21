from io import BytesIO

import pandas as pd

from reportlab.lib.pagesizes import A4

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from xml.sax.saxutils import escape


def safe_text(text):

    return escape(
        str(text)
    ).replace(
        "\n",
        "<br/>"
    )


def create_pdf(study_pack):

    buffer = BytesIO()


    document = SimpleDocTemplate(

        buffer,

        pagesize=A4,

        rightMargin=40,

        leftMargin=40,

        topMargin=40,

        bottomMargin=40
    )


    styles = getSampleStyleSheet()


    story = []


    # Title

    story.append(

        Paragraph(

            safe_text(
                study_pack.title
            ),

            styles["Title"]
        )
    )


    story.append(
        Spacer(1, 20)
    )


    # Summary

    story.append(

        Paragraph(

            "Summary Notes",

            styles["Heading2"]
        )
    )


    story.append(

        Paragraph(

            safe_text(
                study_pack.summary_notes
            ),

            styles["BodyText"]
        )
    )


    story.append(
        PageBreak()
    )


    # MCQs

    story.append(

        Paragraph(

            "20 Practice MCQs",

            styles["Heading2"]
        )
    )


    for index, mcq in enumerate(

        study_pack.mcqs,

        start=1
    ):


        story.append(

            Paragraph(

                f"<b>{index}. "
                f"{safe_text(mcq.question)}</b>",

                styles["BodyText"]
            )
        )


        story.append(

            Paragraph(

                f"A. {safe_text(mcq.option_a)}",

                styles["BodyText"]
            )
        )


        story.append(

            Paragraph(

                f"B. {safe_text(mcq.option_b)}",

                styles["BodyText"]
            )
        )


        story.append(

            Paragraph(

                f"C. {safe_text(mcq.option_c)}",

                styles["BodyText"]
            )
        )


        story.append(

            Paragraph(

                f"D. {safe_text(mcq.option_d)}",

                styles["BodyText"]
            )
        )


        story.append(

            Paragraph(

                f"<b>Answer:</b> "
                f"{safe_text(mcq.correct_answer)}",

                styles["BodyText"]
            )
        )


        story.append(

            Paragraph(

                f"<b>Explanation:</b> "
                f"{safe_text(mcq.explanation)}",

                styles["BodyText"]
            )
        )


        story.append(
            Spacer(1, 10)
        )


    story.append(
        PageBreak()
    )


    # Short Answers

    story.append(

        Paragraph(

            "5 Short-Answer Questions",

            styles["Heading2"]
        )
    )


    for index, item in enumerate(

        study_pack.short_answers,

        start=1
    ):


        story.append(

            Paragraph(

                f"<b>{index}. "
                f"{safe_text(item.question)}</b>",

                styles["BodyText"]
            )
        )


        story.append(

            Paragraph(

                f"<b>Model Answer:</b> "
                f"{safe_text(item.model_answer)}",

                styles["BodyText"]
            )
        )


        story.append(
            Spacer(1, 10)
        )


    story.append(
        PageBreak()
    )


    # Glossary

    story.append(

        Paragraph(

            "Key Terms Glossary",

            styles["Heading2"]
        )
    )


    for item in study_pack.glossary:


        story.append(

            Paragraph(

                f"<b>{safe_text(item.term)}</b>: "
                f"{safe_text(item.definition)}",

                styles["BodyText"]
            )
        )


        story.append(
            Spacer(1, 8)
        )


    story.append(
        PageBreak()
    )


    # Study Order

    story.append(

        Paragraph(

            "Suggested Study Order",

            styles["Heading2"]
        )
    )


    for step in study_pack.study_order:


        story.append(

            Paragraph(

                f"<b>{step.step_number}. "
                f"{safe_text(step.topic)}</b>",

                styles["BodyText"]
            )
        )


        story.append(

            Paragraph(

                safe_text(step.reason),

                styles["BodyText"]
            )
        )


        story.append(
            Spacer(1, 8)
        )


    document.build(story)


    buffer.seek(0)


    return buffer.getvalue()


def create_mcq_csv(study_pack):

    rows = []


    for mcq in study_pack.mcqs:

        rows.append({

            "Question":
                mcq.question,

            "Option A":
                mcq.option_a,

            "Option B":
                mcq.option_b,

            "Option C":
                mcq.option_c,

            "Option D":
                mcq.option_d,

            "Correct Answer":
                mcq.correct_answer,

            "Explanation":
                mcq.explanation
        })


    dataframe = pd.DataFrame(rows)


    return dataframe.to_csv(
        index=False
    ).encode("utf-8")