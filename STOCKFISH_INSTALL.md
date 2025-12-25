# Installing Stockfish Chess Engine

## Quick Installation

Since you're on Fedora, run:
```bash
sudo dnf install stockfish
```

Then verify the installation:
```bash
python test_setup.py
```

## Alternative Installation Methods

### Package Managers

**Fedora/RHEL/CentOS:**
```bash
sudo dnf install stockfish
```

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install stockfish
```

**Arch Linux:**
```bash
sudo pacman -S stockfish
```

**macOS with Homebrew:**
```bash
brew install stockfish
```

### Manual Installation

1. **Download Stockfish:**
   - Visit: https://stockfishchess.org/download/
   - Choose your platform (Linux x64 for you)

2. **Extract and Install:**
   ```bash
   # Example for manual installation
   wget https://stockfishchess.org/files/stockfish_15_linux_x64_avx2.zip
   unzip stockfish_15_linux_x64_avx2.zip
   sudo cp stockfish_15_linux_x64_avx2/stockfish_15_linux_x64_avx2 /usr/local/bin/stockfish
   sudo chmod +x /usr/local/bin/stockfish
   ```

3. **Update Configuration:**
   If you install Stockfish in a custom location, update the path in [Clean.py](Clean.py):
   ```python
   STOCKFISH_PATH = Path("/path/to/your/stockfish")
   ```

## Troubleshooting

**Command not found:**
- Make sure Stockfish is in your PATH
- Check the STOCKFISH_PATH variable in Clean.py
- Run `which stockfish` to find the installed location

**Permission denied:**
- Make sure the Stockfish binary is executable: `chmod +x /path/to/stockfish`

**Version compatibility:**
- This project works with Stockfish 14+
- Check your version: `stockfish --version`

## Verifying Installation

Run the test script to verify everything is working:
```bash
python test_setup.py
```

You should see:
```
✅ Stockfish found at: /usr/bin/stockfish
```