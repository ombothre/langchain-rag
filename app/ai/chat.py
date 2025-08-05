from ai.components.chain import Chain

def load_chain():
    retrieval_chain = Chain.get_retrival_chain()
    return retrieval_chain

def chat(query: str):
    chain = load_chain()
    response = chain.invoke({"input": query})
    print(response)
    return response["answer"]
