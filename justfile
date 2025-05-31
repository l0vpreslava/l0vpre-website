[working-directory: '.']
serve:
    uv run fastapi dev src/website

[working-directory: '.']
check:
    uv run mypy .

[working-directory: '.']
fmt:
    uv run black .

prepare: fmt check
