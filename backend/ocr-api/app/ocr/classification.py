import re


def classify_document(text: str) -> str:
    """
    Classify the type of document based on its text.

    Args:
        text (str): Extracted text from the document.

    Returns:
        str: Document type ("Aadhaar", "PAN", "Passport", or "Unknown").
    """
    if re.search(r"\d{4} \d{4} \d{4}", text):
        return "Aadhaar"
    elif re.search(r"[A-Z]{5}\d{4}[A-Z]", text):
        return "PAN"
    elif re.search(r"[A-Z]\d{7}", text):
        return "Passport"
    else:
        return "Unknown"
