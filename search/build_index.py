"""Old phase-1 script: build index.json from the PDFs in ../pdfs
Run from the search/ folder:  python build_index.py
"""
from indexing.loader import load_collection
from indexing.preprocessing import process
from indexing.indexer import build_inverted_file, save_index


def main():
    collection = load_collection("../pdfs")
    print(f"Loaded {len(collection)} documents")

    docs = {}
    for doc_id, info in collection.items():
        docs[doc_id] = process(info["text"])
        print(f"  {doc_id} {info['path']}: {len(docs[doc_id])} terms")

    index = build_inverted_file(docs)
    save_index(index, "index.json")
    print(f"Index saved: {len(index['dictionary'])} unique terms → index.json")


if __name__ == "__main__":
    main()
