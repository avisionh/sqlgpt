import os
import argparse

from datetime import datetime

import src.constants as constants

from langchain.sql_database import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit

from langchain_community.chat_models import ChatOllama
from langchain.agents import create_sql_agent
from langchain.agents.agent_types import AgentType


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
    handle_parsing_errors=True,
)


if __name__ == """__main__""":
    argp = argparse.ArgumentParser()
    argp.add_argument(
        "-uq",
        "--user_question",
        type=str,
        help="What's the data question you want to ask?",
    )
    args = argp.parse_args()

    start_time = datetime.now()
    agent.invoke(input={"input": args.user_question})
    end_time = datetime.now()
    print(
        f"It took me {(end_time - start_time).total_seconds()} seconds "
        f"to think through your question and give you an answer."
    )
