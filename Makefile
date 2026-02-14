.PHONY: install test lint format check test-files

install:
	uv sync

test:
	uv run pytest -v

lint:
	uv run ruff check .

format:
	uv run ruff format .

check: lint test

test-files:
	@echo "Creating test files..."
	@mkdir -p tests/fixtures
	@echo '{"host": "hexlet.io", "timeout": 50}' > file1.json
	@echo '{"host": "hexlet.io", "timeout": 20}' > file2.json
	@echo 'host: hexlet.io\ntimeout: 50' > file1.yml
	@echo 'host: hexlet.io\ntimeout: 20' > file2.yml
	@echo "Done!"