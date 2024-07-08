import src.constants as constants

from langchain.sql_database import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit

from langchain_community.chat_models import ChatOllama
from langchain.agents import create_sql_agent
from langchain.agents.agent_types import AgentType

import streamlit as st
from langchain_community.callbacks import StreamlitCallbackHandler


def run_app():
    st.title(body="sqlGPT")

    # backend
    db = SQLDatabase.from_uri(
        database_uri=constants.SQLALCHEMY_URL, sample_rows_in_table_info=15
    )
    llm = ChatOllama(
        base_url=constants.OLLAMA_HOST_LOCAL,
        model=constants.LLM_MODEL,
        top_k=constants.TOP_K,
        top_p=constants.TOP_P,
        temperature=constants.TEMPERATURE,
        repeat_penalty=constants.REPEAT_PENALTY,
    )
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)

    agent = create_sql_agent(
        llm=llm,
        toolkit=toolkit,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )

    # frontend
    # initialise chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(name=message["role"]):
            st.markdown(body=message["content"])
    # react to user input
    if question := st.chat_input(placeholder="Enter our question"):
        # display user message in chat message container
        with st.chat_message(name="user", avatar="💅"):
            st.markdown(body=question)
        # add user message to chat message
        st.session_state.messages.append({"role": "user", "content": question})
        # add chatbot's response, displaying in message container
        with st.chat_message(name="ai", avatar="🦖"):
            st_callback = StreamlitCallbackHandler(st.container())
            response = agent.invoke(input=question, callbacks=[st_callback])
            st.write(response)
        # add chatbot's response to chat history
        st.session_state.messages.append({"role": "ai", "content": response})


if __name__ == "__main__":
    run_app()
