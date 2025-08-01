import streamlit as st
import nltk
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters.nltk import NLTKTextSplitter
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain.chains.conversation.base import ConversationChain
from prompts.prompts import templates
from PyPDF2 import PdfReader
from prompts.prompt_selector import prompt_sector


def embedding(text):
    """Creates embeddings for a given text."""
    text_splitter = NLTKTextSplitter()
    texts = text_splitter.split_text(text)
    # Create embeddings
    embeddings = OpenAIEmbeddings()
    docsearch = FAISS.from_texts(texts, embeddings)
    return docsearch


def resume_reader(resume):
    """Extracts text from a PDF resume."""
    pdf_reader = PdfReader(resume)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text


def initialize_session_state(template=None, position=None):
    """
    Initializes all session state variables, ensuring each is created only once.
    This prevents unnecessary re-computation and API calls on every Streamlit rerun.
    """
    if 'docsearch' not in st.session_state:
        if 'jd' in st.session_state:
            st.session_state.docsearch = embedding(st.session_state.jd)
        else:
            st.session_state.docsearch = embedding(resume_reader(st.session_state.resume))

    if 'retriever' not in st.session_state:
        st.session_state.retriever = st.session_state.docsearch.as_retriever(search_type="similarity")

    if 'chain_type_kwargs' not in st.session_state:
        if 'jd' in st.session_state:
            Interview_Prompt = PromptTemplate(input_variables=["context", "question"],
                                              template=template)
            st.session_state.chain_type_kwargs = {"prompt": Interview_Prompt}
        else:
            st.session_state.chain_type_kwargs = prompt_sector(position, templates)

    if 'memory' not in st.session_state:
        st.session_state.memory = ConversationBufferMemory()

    if "history" not in st.session_state:
        st.session_state.history = []

    if "token_count" not in st.session_state:
        st.session_state.token_count = 0

    if "guideline" not in st.session_state:
        llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.6)
        st.session_state.guideline = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type_kwargs=st.session_state.chain_type_kwargs, chain_type='stuff',
            retriever=st.session_state.retriever, memory=st.session_state.memory).run(
            "Create an interview guideline and prepare only one questions for each topic. Make sure the questions tests the technical knowledge")

    if "screen" not in st.session_state:
        llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.8)
        PROMPT = PromptTemplate(
            input_variables=["history", "input"],
            template="""I want you to act as an interviewer strictly following the guideline in the current conversation.

                            Ask me questions and wait for my answers like a real person.
                            Do not write explanations.
                            Ask question like a real person, only one question at a time.
                            Do not ask the same question.
                            Do not repeat the question.
                            Do ask follow-up questions if necessary.
                            You name is GPTInterviewer.
                            I want you to only reply as an interviewer.
                            Do not write all the conversation at once.
                            If there is an error, point it out.

                            Current Conversation:
                            {history}

                            Candidate: {input}
                            AI: """
        )
        st.session_state.screen = ConversationChain(prompt=PROMPT, llm=llm,
                                                    memory=st.session_state.memory)

    if "feedback" not in st.session_state:
        llm = ChatOpenAI(
            model_name="gpt-3.5-turbo",
            temperature=0.5, )
        st.session_state.feedback = ConversationChain(
            prompt=PromptTemplate(input_variables=["history", "input"], template=templates.feedback_template),
            llm=llm,
            memory=st.session_state.memory,
        )
