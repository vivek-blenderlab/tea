
import streamlit as st

from langchain_openai import ChatOpenAI
from langchain.agents import (
    create_openai_tools_agent,
    AgentExecutor
)



def send_email():
    st.write("Email agent running")
