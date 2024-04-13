#!/usr/bin/env bash

if [ -z "$PROJECT_DIR" ]; then
    echo "PROJECT_DIR is not set. Please set it and rerun the script."
    exit 1
fi

if [ ! -d "$PROJECT_DIR" ]; then
    echo "Error: The directory specified in PROJECT_DIR does not exist."
    exit 1
fi

if ! command -v pip &> /dev/null
then
    echo "pip could not be found, please install it."
    exit 1
fi


if pip freeze > "$PROJECT_DIR/requirements.txt"; then
    echo "requirements.txt has been updated successfully in $PROJECT_DIR."
else
    echo "Failed to update requirements.txt."
    exit 1
fi
