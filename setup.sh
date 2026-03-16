#!/bin/bash
# Setup script for CV generation system

echo "Setting up CV generation system..."
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3 first."
    exit 1
fi

echo "✓ Python 3 found"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo "✓ Virtual environment created"
else
    echo "✓ Virtual environment already exists"
fi

# Activate virtual environment and install dependencies
echo "Installing dependencies..."
source venv/bin/activate
pip install pyyaml > /dev/null 2>&1

if [ $? -eq 0 ]; then
    echo "✓ Dependencies installed"
else
    echo "❌ Failed to install dependencies"
    exit 1
fi

echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "  1. Edit cv-data.yaml with your information"
echo "  2. Run: make html (or ./generate.sh)"
echo "  3. Open cv-output.html in your browser"
echo "  4. Print to PDF (Ctrl+P / Cmd+P)"
echo ""
