from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
from config.settings import utils

template = """You are EaseMyAI's official chatbot, designed to help users understand the company, its services, and how it can assist them.

Use only the context below to answer the user's question. 
If the context does not contain relevant information, respond with:
"I’m sorry, I couldn’t find an answer based on the available information."

Be brief, accurate, and helpful.

----------------------
Context:
{context}

Question: {input}

Answer:"""

def get_prompt() -> PromptTemplate:
    return PromptTemplate.from_template(template)

class LLM:
    @classmethod
    def get_llm(cls,model: str = "phi3"):
        return OllamaLLM(model=model, base_url=utils.OLLAMA_API, temperature=0.4)
