setup:
    uv sync --locked
    go mod download

lint:
    uv run ruff check .
    uv run rumdl check .
    go tool actionlint

format:
    uv run ruff format .
    uv run rumdl fmt .
    go tool yamlfmt .

check: lint
    uv run ruff format --check .
    go tool yamlfmt -lint .