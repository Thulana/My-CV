#!/bin/bash
# Simple script to generate HTML resume

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Virtual environment not found. Running setup..."
    ./setup.sh
fi

# Activate virtual environment and generate HTML
source venv/bin/activate
python generate_html.py

# Open in browser (optional)
if [ "$1" == "--open" ]; then
    if command -v open &> /dev/null; then
        open cv-output.html
    elif command -v xdg-open &> /dev/null; then
        xdg-open cv-output.html
    else
        echo "Please open cv-output.html manually"
    fi
fi
