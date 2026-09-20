setup:
    uv sync --locked

lint:
    uv run ruff check .
    uv run rumdl check .

format:
    uv run ruff format .
    uv run rumdl fmt .

check: lint
    uv run ruff format --check .