FROM python:latest

WORKDIR /app

ENV PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on

COPY . .
RUN pip install poetry
RUN poetry install --no-interaction --no-ansi

EXPOSE 8501
ENTRYPOINT ["poetry", "run", "streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
CMD ["sleep", "100000"]
