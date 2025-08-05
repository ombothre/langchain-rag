from langchain_community.document_loaders import TextLoader
from langchain_core.documents import Document
from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter
import json
from services.rag_setup.vectordb import VectorDB
from typing import Optional

def get_jsonl_documents(path: Path) -> list[Document]:
    documents = []
    for file in path.iterdir():
        if file.suffix == ".jsonl":
            with open(file, "r", encoding="utf-8") as f:
                for line in f:
                    try:
                        entry = json.loads(line)
                        text = entry.get("text", "").strip()
                        source = entry.get("url", "unknown")
                        if text:
                            documents.append(Document(page_content=text, metadata={"source": source}))
                    except json.JSONDecodeError as e:
                        print(f"JSON decode error in {file.name}: {e}")
    return documents

def get_txt_documents(path: Path) -> list[Document]:
    documents = []
    for file in path.iterdir():
        if file.suffix == ".txt":
            documents.extend(TextLoader(file_path=str(file), encoding="utf-8").load())
    return documents

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100,
    separators=["\n\n", "\n", " ", ""]
)

class Processor:
    def __init__(self, jsonl_path: Optional[Path] = None, txt_path: Optional[Path] = None) -> None:
        if jsonl_path:
            json_docs = get_jsonl_documents(jsonl_path)
        # txt_docs = get_txt_documents(txt_path)
        self.documents: list[Document] = json_docs

        print(f"Total loaded documents: {len(self.documents)}")

        raw_chunks = text_splitter.split_documents(self.documents)
        self.chunked_documents = [
            Document(page_content=doc.page_content.lower(), metadata=doc.metadata)
            for doc in raw_chunks
        ]
    
        print(f"Total chunks: {len(self.chunked_documents)}")

    def get_chunked_documents(self) -> list[Document]:
        return self.chunked_documents
