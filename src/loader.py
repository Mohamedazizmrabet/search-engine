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
    collection = {}
    files = sorted(Path(folder).glob("*.txt"))

    for i, path in enumerate(files, start=1):
        print(f"{i} {path.as_posix()}")
        text = path.read_text(encoding="utf-8")
        doc_id = f"D{i}"
        collection[doc_id] = {
            "path": path.as_posix(),
            "lang": detect_language(text),
            "text": text,
        }

    return collection
"""Read every .txt file in `folder`.
   Returns {"D1": {"path": ..., "lang": ..., "text": ...}, ...}
"""