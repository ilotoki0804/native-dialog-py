default:
    just --list

init:
    uv venv .venv -p 3.13

activate:
    source ./.venv/bin/activate

test: activate dev
    python -c "import native_dialog"

dev:
    uvx maturin develop

build:
    uv build

publish: build
    uv publish
