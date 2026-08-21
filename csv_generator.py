import pandas as pd
from io import StringIO


def create_mcq_csv(study_pack):

    rows = []

    for mcq in study_pack.mcqs:

        rows.append(
            {
                "Question": mcq.question,
                "Option A": mcq.option_a,
                "Option B": mcq.option_b,
                "Option C": mcq.option_c,
                "Option D": mcq.option_d,
                "Correct Answer": mcq.correct_answer,
                "Explanation": mcq.explanation
            }
        )

    dataframe = pd.DataFrame(rows)

    return dataframe.to_csv(
        index=False
    ).encode("utf-8")