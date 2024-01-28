import os
from dotenv import load_dotenv

from src.constants import SQLALCHEMY_URL

from langchain.sql_database import SQLDatabase


# pass in API key
load_dotenv(dotenv_path=".env")
API_KEY = os.environ.get("OPENAI_API_KEY")

db = SQLDatabase.from_uri(database_uri=SQLALCHEMY_URL)
