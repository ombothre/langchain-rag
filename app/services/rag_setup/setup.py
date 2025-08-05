from pathlib import Path
from services.rag_setup.processor import Processor
from services.rag_setup.vectordb import VectorDB

txt_path = Path("services/scraper/data/visible_text")
jsonl_path = Path("services/scraper/data/jsonl_data")

def vector_setup():

    processor = Processor(jsonl_path=jsonl_path)
    docs = processor.get_chunked_documents()

    vector_db = VectorDB.create(chunks=docs)