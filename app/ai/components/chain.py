from ai.components.llm import LLM, get_prompt
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from ai.components.retriever import Retriever

class Chain:
    @classmethod
    def get_combined_chain(cls):
        return create_stuff_documents_chain(
            llm=LLM.get_llm(),
            prompt=get_prompt()
    )

    @classmethod
    def get_retrival_chain(cls):
        retriever = Retriever()
        return create_retrieval_chain(
            retriever=retriever.get_retriever(),
            combine_docs_chain=cls.get_combined_chain()
        )
     
     