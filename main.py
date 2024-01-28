import os
import argparse
from dotenv import load_dotenv

from datetime import datetime

from src.constants import SQLALCHEMY_URL, GPT_MODEL

from langchain.sql_database import SQLDatabase

from langchain_openai import ChatOpenAI
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain.agents import create_sql_agent


# pass in API key
load_dotenv(dotenv_path=".env")
API_KEY = os.environ.get("OPENAI_API_KEY")

db = SQLDatabase.from_uri(database_uri=SQLALCHEMY_URL)
llm = ChatOpenAI(model=GPT_MODEL, temperature=0, api_key=API_KEY)
toolkit = SQLDatabaseToolkit(db=db, llm=llm)

agent = create_sql_agent(llm=llm, toolkit=toolkit, verbose=True, top_k=100)


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
