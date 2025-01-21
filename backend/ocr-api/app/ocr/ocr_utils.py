from PIL import Image
import pytesseract
import ftfy


def perform_ocr(image_path: str) -> str:
    """
    Perform OCR on the input image.

    Args:
        image_path (str): Path to the preprocessed image.

    Returns:
        str: Extracted text.
    """
    # Run OCR
    pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

    text = pytesseract.image_to_string(Image.open(image_path), lang="eng")

    # Clean the text using ftfy
    text = ftfy.fix_text(text)
    text = ftfy.fix_encoding(text)

    return text
