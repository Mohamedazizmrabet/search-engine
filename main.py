"""Build the index: python main.py"""
from src.loader import load_collection
from src.preprocessing import process
from src.indexer import build_inverted_file, save_index


def main():
    collection = load_collection("data")
    print(f"Loaded {len(collection)} documents")

    docs = {}
    for doc_id, info in collection.items():
        docs[doc_id] = process(info["text"], info["lang"])
        print(f"  {doc_id} [{info['lang']}] {info['path']}: {len(docs[doc_id])} terms")

    index = build_inverted_file(docs)
    save_index(index, "index.json")
    print(f"Index saved: {len(index['dictionary'])} unique terms → index.json")


if __name__ == "__main__":
    main()
