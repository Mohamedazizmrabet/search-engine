"""Step 1 — Load the collection and detect each document's language.
Owner: Member A
"""
from pathlib import Path
from langdetect import detect, DetectorFactory

DetectorFactory.seed = 0  # same result on every run


def detect_language(text: str) -> str:
    """Return "fr" or "en". Anything else (or an error) falls back to "en"."""
    try:
        lang = detect(text)
    except Exception:
        return "en"
    return lang if lang in ("fr", "en") else "en"


def load_collection(folder: str = "data") -> dict:
    """Read every .txt file in `folder`.

    Returns:
        {"D1": {"path": "data/a.txt", "lang": "fr", "text": "..."}, ...}
    Files are sorted by name so IDs stay stable between runs.
    """
    # TODO (A): loop over sorted(Path(folder).glob("*.txt")),
    #           read with encoding="utf-8", detect language, build the dict
    raise NotImplementedError
