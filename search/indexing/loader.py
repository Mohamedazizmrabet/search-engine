from pathlib import Path
from pypdf import PdfReader


def read_pdf(path: Path) -> str:
    """Extract the text of every page of a PDF and join it."""
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text = text + page_text + "\n"
    return text


def load_collection(folder: str = "data") -> dict:
    """Read every .pdf file in `folder`.
    Returns {"D1": {"path": ..., "text": ...}, ...}
    """
    collection = {}
    files = sorted(Path(folder).glob("*.pdf"))

    for i, path in enumerate(files, start=1):
        text = read_pdf(path)
        doc_id = f"D{i}"
        collection[doc_id] = {
            "path": path.as_posix(),
            "text": text,
        }

    return collection


if __name__ == "__main__":
    print(load_collection("data"))