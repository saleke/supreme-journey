#!/usr/bin/env bash

echo '=============================================='
echo '                 Running                      '
echo '=============================================='
echo "=== Displaying pip Version ==="
pip --version

echo ''

TARGET_PATH='local_lib'
PYTHON_SCRIPT='my_program.py'
LOG_FILE='installation.log'



if [ -d "$TARGET_PATH" ]; then

    echo "Existing local_lib folder found. Crushing old install..."

    rm -rf "$TARGET_PATH"
fi

mkdir "$TARGET_PATH"
echo "Installing the 'path' development version from GitHub..."

pip install --target "$TARGET_PATH" --upgrade --force-reinstall git+https://github.com/jaraco/path > "$LOG_FILE" 2>&1 || exit 1

if [ $? -eq 0 ]; then
    echo "Installation successful! Executing your program..."
    echo "--------------------------------------------------"
    
    python3 "$PYTHON_SCRIPT"
else
    echo "Error: Installation failed. See '$LOG_FILE' for details."
    exit 1
fi


echo "=== Installation Completed successfully! ==="
