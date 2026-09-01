#!/usr/bin/env bash

TARGET_PATH="local_lib"
PYTHON_SCRIPT="my_program.py"

echo "====================== Running ============================"
echo "checking if local $TARGET_PATH exists"

if [ -d "$TARGET_PATH" ]; then
    echo "found local file $TARGET_PATH"
    echo "deleting $TARGET_PATH"

    rm -rf "$TARGET_PATH"
    echo "deleted"
fi
mkdir "local_lib"

echo "====================== Installing path library ============================"
pip install --target "$TARGET_PATH" --force-reinstall git+https://github.com/jaraco/path > "installation_log.log" 2>&1 || echo "error: failed to install"

if [ $? -eq 0 ]; then
    echo "package installed successfully"
fi

python3 "$PYTHON_SCRIPT"
