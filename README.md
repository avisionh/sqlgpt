# sqlgpt
Translating natural language into a query and then executing this in a database.

## Getting started
Create an OpenAI API token [here](https://platform.openai.com/api-keys) and store it by creating an `.env` file with the following contents:
```commandline
OPENAI_API_KEY=<your_openai_api_key>
```

Create a service account key for the project in GCP that you want to access [here](https://cloud.google.com/iam/docs/keys-create-delete). Then store this in as `gcp_service_account_key.json`.

Update the `src/constants.py` file with the project and dataset that teh service account key as access to.

Now set-up the project by runnng the following:
```commandline
poetry shell
poetry run
```
