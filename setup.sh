#!/bin/bash
# ORIOS Project Setup Script
# Creates virtual environment and installs dependencies

set -e  # Exit on error

echo "🚀 Setting up ORIOS project..."
echo ""

# Check Python version
echo "📌 Checking Python version..."
python3 --version

if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed"
    exit 1
fi

# Create virtual environment
echo ""
echo "📦 Creating virtual environment..."
if [ -d "venv" ]; then
    echo "⚠️  Virtual environment already exists. Removing..."
    rm -rf venv
fi
python3 -m venv venv

# Activate virtual environment
echo ""
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo ""
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo ""
echo "📥 Installing dependencies from requirements.txt..."
pip install -r requirements.txt

# Verify installation
echo ""
echo "✅ Verifying installation..."
python3 -c "import matplotlib; import numpy; print(f'matplotlib: {matplotlib.__version__}'); print(f'numpy: {numpy.__version__}')"

# Test script
echo ""
echo "🧪 Testing chart generation..."
python3 create_ideation_quality_chart.py

echo ""
echo "✨ Setup complete!"
echo ""
echo "To activate the virtual environment in the future, run:"
echo "  source venv/bin/activate"
echo ""
echo "To deactivate, run:"
echo "  deactivate"
echo ""
