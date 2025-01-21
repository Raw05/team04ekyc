import cv2
import os


def preprocess_image(image_path: str, preprocess: str = "thresh") -> str:
    """
    Preprocess the image for OCR.

    Args:
        image_path (str): Path to the input image.
        preprocess (str): Preprocessing method. Options: "thresh", "adaptive", "linear", "cubic", "blur", "bilateral", "gauss".

    Returns:
        str: Path to the preprocessed image.
    """
    # Load the image
    image = cv2.imread(image_path)
    print(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply preprocessing method
    if preprocess == "thresh":
        gray = cv2.threshold(
            gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    elif preprocess == "adaptive":
        gray = cv2.adaptiveThreshold(
            gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    elif preprocess == "linear":
        gray = cv2.resize(gray, None, fx=2, fy=2,
                          interpolation=cv2.INTER_LINEAR)
    elif preprocess == "cubic":
        gray = cv2.resize(gray, None, fx=2, fy=2,
                          interpolation=cv2.INTER_CUBIC)
    elif preprocess == "blur":
        gray = cv2.medianBlur(gray, 3)
    elif preprocess == "bilateral":
        gray = cv2.bilateralFilter(gray, 9, 75, 75)
    elif preprocess == "gauss":
        gray = cv2.GaussianBlur(gray, (5, 5), 0)
    else:
        raise ValueError(f"Invalid preprocessing type: {preprocess}")

    # Save the preprocessed image
    processed_image_path = f"{os.path.splitext(image_path)[0]}_processed.png"
    cv2.imwrite(processed_image_path, gray)

    return processed_image_path
