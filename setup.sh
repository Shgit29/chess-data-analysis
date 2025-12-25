#!/bin/bash
set -e

echo "🚀 Setting up Chess Data Analysis Project..."

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check if Python is available
if ! command_exists python3; then
    echo "❌ Error: Python 3 is required but not installed."
    exit 1
fi

# Install Stockfish based on distribution
echo "📦 Installing Stockfish engine..."

if command_exists dnf; then
    # Fedora/RHEL
    sudo dnf install -y stockfish
    STOCKFISH_PATH="/usr/bin/stockfish"
elif command_exists apt; then
    # Ubuntu/Debian
    sudo apt update && sudo apt install -y stockfish
    STOCKFISH_PATH="/usr/games/stockfish"
elif command_exists pacman; then
    # Arch Linux
    sudo pacman -S --noconfirm stockfish
    STOCKFISH_PATH="/usr/bin/stockfish"
elif command_exists brew; then
    # macOS with Homebrew
    brew install stockfish
    STOCKFISH_PATH="/opt/homebrew/bin/stockfish"
else
    echo "⚠️  Could not detect package manager. Please install Stockfish manually from https://stockfishchess.org/download/"
    echo "Then update the STOCKFISH_PATH in Clean.py"
    STOCKFISH_PATH="stockfish"  # Hope it's in PATH
fi

# Update the Stockfish path in Clean.py
if [ -f "Clean.py" ]; then
    echo "🔧 Updating Stockfish path in Clean.py..."
    sed -i "s|STOCKFISH_PATH = Path(.*|STOCKFISH_PATH = Path(\"$STOCKFISH_PATH\")|" Clean.py
fi

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "🐍 Creating Python virtual environment..."
    python3 -m venv .venv
fi

# Activate virtual environment and install dependencies
echo "📋 Installing Python dependencies..."
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# Verify Stockfish installation
echo "✅ Verifying Stockfish installation..."
if command_exists stockfish || [ -f "$STOCKFISH_PATH" ]; then
    echo "✅ Stockfish engine installed successfully at: $STOCKFISH_PATH"
else
    echo "⚠️  Stockfish installation could not be verified. Please check manually."
fi

echo ""
echo "🎉 Setup complete! To get started:"
echo ""
echo "1. Activate the virtual environment:"
echo "   source .venv/bin/activate"
echo ""
echo "2. Place your PGN files (MAF13-white.pgn, MAF13-black.pgn) in the project directory"
echo ""
echo "3. Run the analysis pipeline:"
echo "   python Clean.py       # Analyze games for errors"
echo "   python Calculation.py # Calculate statistics"
echo "   python Analytics.py   # Generate analytics"
echo "   python Openings.py    # Analyze openings"
echo ""
echo "For more information, see README.md"