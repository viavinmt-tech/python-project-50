.PHONY: install test lint format check test-coverage

install:
	uv sync --dev

test:
	uv run python -m pytest tests/ -v --cov=gendiff

lint:
	uv run ruff check .

format:
	uv run ruff check --fix .
	uv run ruff format .

check: lint test

test-coverage:
	uv run python -m pytest tests/ -v --cov=gendiff --cov-report=xml --cov-report=term-missing
