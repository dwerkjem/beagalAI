#!/usr/bin/env bash
if [ -z "$PROJECT_DIR" ]; then
    echo "PROJECT_DIR is not set. Please set it and rerun the script."
    exit 1
fi

# pip freeze
pip freeze > "$PROJECT_DIR"/requirements.txt
echo "requirements.txt has been updated."