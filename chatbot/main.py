import streamlit as st
from chatbot import chat  # import your chat() function

st.set_page_config(page_title="What's Your Paper?", page_icon="📘")

# Title and subtitle
st.title("📘 What's Your Paper?")
st.markdown("Ask any question about your research paper Attention Is All You Need 2017. This chatbot will read and respond based on its understanding.")

# Input box
query = st.text_input("Ask a question:", placeholder="e.g., What is the main contribution of this paper?")

if query:
    with st.spinner("Thinking..."):
        answer = chat(query)
    st.success("Answer:")
    st.write(answer)

# Footer
st.markdown("---")
st.caption("Built with 💬 sentence-transformers, 🤗 transformers, and 🧠 Streamlit.")
