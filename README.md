# Project Euler Solutions

My solutions to [Project Euler](https://projecteuler.net/) problems in Python.

## Prerequisites

Install `uv` and `just`:

```shell
curl -LsSf https://astral.sh/uv/install.sh | sh
uv tool install rust-just
```

## Setup

Run from the repo root:

```shell
just setup
```

## Usage

```shell
just lint   # Lint Python and Markdown
just format # Format Python and Markdown
just check  # Run lint and formatting checks
```
