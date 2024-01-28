setup local:
	@poetry --version || pip install poetry
	poetry shell
	@echo "Installing package dependencies..."
	poetry install
	@echo "Installing pre-commit hooks..."
	pre-commit install
