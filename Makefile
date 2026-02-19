.PHONY: install test lint format check

install:
	uv sync --dev

test:
	uv run pytest tests/ -v

test-coverage:
	uv run pytest --cov=gendiff tests/ --cov-report=term-missing

lint:
	uv run ruff check .

format:
	uv run ruff format .

check: lint test

