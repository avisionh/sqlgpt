# sqlgpt
Translating natural language into a query and then executing this in a database.

## Getting started
Download Ollama from the official website [here](https://ollama.com/download).

In your terminal, download Llama 3 via `ollama pull llama3` (takes ~30 mins to download).

Create a service account key for the project in GCP that you want to access [here](https://cloud.google.com/iam/docs/keys-create-delete). Then store this in as `gcp_service_account_key.json`.

Update the `src/constants.py` file with the project and dataset that the service account key has access to.

Now set-up the project by running the following:
```commandline
make setup-local
```

### Getting data from SQL
To ask the Llama3 a question about your data, run the following in your terminal:
```commandline
poetry run python main.py --user_question "<your_question>"
```
