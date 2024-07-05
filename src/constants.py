PROJECT = "bigquery-public-data"
DATASET = "bls"
SERVICE_ACCOUNT_FILE = "profiles/dummy-project-428510-4418e1b4f381.json"
SQLALCHEMY_URL = (
    f"bigquery://{PROJECT}/{DATASET}?credentials_path={SERVICE_ACCOUNT_FILE}"
)

LLM_MODEL = "llama3:8b"
OLLAMA_HOST_LOCAL = "http://localhost:11434"
TOP_K = 30
TOP_P = 0.9
TEMPERATURE = 0.2
REPEAT_PENALTY = 0.9
