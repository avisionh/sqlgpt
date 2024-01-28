PROJECT = "<your_project>"
DATASET = "<your_dataset>"
SERVICE_ACCOUNT_FILE = "gcp_service_account_key.json"
SQLALCHEMY_URL = (
    f"bigquery://{PROJECT}/{DATASET}?credentials_path={SERVICE_ACCOUNT_FILE}"
)

GPT_MODEL = "gpt-3.5-turbo-1106"
