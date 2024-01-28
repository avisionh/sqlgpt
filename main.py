import os
from dotenv import load_dotenv

# pass in API key
load_dotenv(dotenv_path=".env")
API_KEY = os.environ.get("OPENAI_API_KEY")
