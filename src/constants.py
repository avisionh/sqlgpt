PROJECT = "<your_project>"
DATASET = "<your_dataset>"
SERVICE_ACCOUNT_FILE = "gcp_service_account_key.json"
SQLALCHEMY_URL = (
    f"bigquery://{PROJECT}/{DATASET}?credentials_path={SERVICE_ACCOUNT_FILE}"
)

LLM_MODEL = "llama3:8b"
OLLAMA_HOST_LOCAL = "http://localhost:11434"
TOP_K = 30
TOP_P = 0.9
TEMPERATURE = 0.2
REPEAT_PENALTY = 0.9
