#install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

#install python for use
uv python install 3.11 3.12

# Lista all version installed in os.
uv python list

# Run one command
uv run --python 3.12 python -c 'print("hello world")'

# Run simple file
uv run scrip.py

# Run and read program from stdin
echo 'print("hello world!")' | uv run -

uv run - <<EOF
print("hello world!")
EOF


# Colocando depedências
uv run --with rich example_deps.py

# ... Com ou sem versões das libs
uv run --with 'rich>12,<13' example_deps.py

