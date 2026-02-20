.PHONY: install test lint format check

install:
	uv sync --dev

test:
	uv run pytest tests/ -v --cov=gendiff

lint:
	uv run ruff check .

format:
	uv run ruff check --fix .
	uv run ruff format .

check: lint test

