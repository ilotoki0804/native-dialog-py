default:
    just --list

init:
    uv venv .venv -p 3.13

activate:
    source ./.venv/bin/activate

test: activate dev
    python -c "import native_dialog; print(native_dialog.alert('title', 'text', 'info'))"

dev:
    uvx maturin develop

build:
    uv build

# https://github.com/PyO3/maturin/issues/2334
publish: build
    uv publish
