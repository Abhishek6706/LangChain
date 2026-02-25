import streamlit as st
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatOpenAI(model='gpt-4.1', temperature= 0.2)

st.header("Research Paper Summariser")

template = PromptTemplate(
    template=
    """Explain the {paper_name} with {style_name} in {length}.
    If paper is not found, return the answer as "NOT FOUND".
    Don't halicunate.
""", input_variables=["paper_name", "style_name", "length"]
)

paper_name = st.selectbox(label="Paper name", options=["Development and Evaluation of ML Models for Cardiotocography Interpretation", "Attention Is All You Need", "BERT"])
style_name = st.selectbox(label="Style name", options=["mathematical", "programatical", "conceptual"])
length = st.selectbox(label= "Length", options=["Long(20 lines)", "medium(10 lines)", "short(5 lines)"])

prompt = template.invoke({
    "paper_name":paper_name,
    "style_name":style_name,
    "length":length
})

if st.button(label="Summarize"):
    result = model.invoke(prompt)
    st.write(result.content)

