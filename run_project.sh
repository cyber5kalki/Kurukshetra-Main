#!/bin/bash
# Ensure Python is available, otherwise set the path to the Python executable
PYTHON_PATH=python3

# Change directory to the Internship-Main directory
cd "$(dirname "$0")/Internship-Main"

# Run the Python scripts
$PYTHON_PATH home.py

# Pause to keep the terminal window open
read -p "Press any key to continue..."

