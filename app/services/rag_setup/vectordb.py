from langchain_ollama import OllamaEmbeddings
from config.settings import utils
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

class VectorDB:

    @classmethod
    def create(cls, chunks: list[Document], model: str = "phi3"):
        try:
            embeddings = OllamaEmbeddings(model=model, base_url=utils.OLLAMA_API)
            db = FAISS.from_documents(documents=chunks, embedding=embeddings)
            db.save_local(utils.INDEX_DIR)
            return cls(db)
        
        except Exception as e:
             print(f"Error adding docs: {str(e)}")

    def __init__(self, vector_store: FAISS) -> None:
        self.vector_store = vector_store
    
    def get_vector_db(self) -> FAISS:
        return self.vector_store