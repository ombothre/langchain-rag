from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from config.settings import utils
from langchain_core.vectorstores.base import VectorStoreRetriever

class Retriever:
    def __init__(self) -> None:
        embeddings = OllamaEmbeddings(model="phi3", base_url=utils.OLLAMA_API)
        vector_db = FAISS.load_local(utils.INDEX_DIR, embeddings, allow_dangerous_deserialization=True)
        self.retriever = vector_db.as_retriever()
    
    def get_retriever(self) -> VectorStoreRetriever:
        return self.retriever