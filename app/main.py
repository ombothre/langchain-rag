import streamlit as st
from ai.chat import load_chain

st.set_page_config(page_title="EaseMyAI Chatbot", layout="centered")
st.title("💬 EaseMyAI Chatbot")
st.caption("Ask me anything about EaseMyAI!")

@st.cache_resource
def load_rag_chain():
    return load_chain()

rag_chain = load_rag_chain()

# Input box
query = st.text_input("Your question", placeholder="e.g., What services does EaseMyAI provide?")

# Run chain
if query:
    with st.spinner("Thinking..."):
        result = rag_chain.invoke({"input": query})
    
    st.markdown("### 💬 Answer")
    st.success(result["answer"])

    with st.expander("📄 Retrieved Documents"):
        for i, doc in enumerate(result["context"]):
            source = doc.metadata.get("source", "unknown")
            st.markdown(f"**Document {i+1}** — Source: `{source}`")
            st.code(doc.page_content.strip()[:1000] + ("..." if len(doc.page_content) > 1000 else ""), language="text")
