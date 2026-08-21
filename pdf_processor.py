from pypdf import PdfReader


MAX_PAGES = 15


def extract_pdf_text(uploaded_file):

    reader = PdfReader(uploaded_file)

    page_count = len(reader.pages)

    if page_count > MAX_PAGES:

        raise ValueError(
            f"This PDF contains {page_count} pages. "
            f"Maximum allowed is {MAX_PAGES} pages."
        )


    extracted_text = []


    for page_number, page in enumerate(
        reader.pages,
        start=1
    ):

        page_text = page.extract_text()

        if page_text:

            extracted_text.append(
                f"--- Page {page_number} ---\n"
                f"{page_text}"
            )


    final_text = "\n\n".join(
        extracted_text
    )


    if not final_text.strip():

        raise ValueError(
            "Could not extract text from this PDF. "
            "The PDF may contain scanned images."
        )


    return final_text