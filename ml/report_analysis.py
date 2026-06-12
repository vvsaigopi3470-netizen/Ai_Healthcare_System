try:
    import pytesseract
except ImportError as exc:
    pytesseract = None
    _PYTESSERACT_IMPORT_ERROR = exc

from PIL import Image

def extract_text(filepath):

    image = Image.open(
        filepath
    )

    text = pytesseract.image_to_string(
        image
    )

    return text