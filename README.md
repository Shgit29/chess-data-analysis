# Chess Data Analysis Project

This project analyzes chess games to identify and study player errors (inaccuracies, mistakes, blunders) using Stockfish engine evaluation.

## Project Structure

- `Clean.py` - Main script for analyzing PGN files and detecting errors using Stockfish
- `Calculation.py` - Processes error data and calculates statistics
- `Analytics.py` - Generates analytical reports and win rates by error types
- `Openings.py` - Analyzes opening performance by color
- `Prescription.py` - (Empty) Future recommendations module

## Data Files

### Input Files
- `MAF13-white.pgn` - PGN file with games where you played as White
- `MAF13-black.pgn` - PGN file with games where you played as Black
- `games_raw.csv` - Raw game data

### Generated Output Files
- `games_with_errors.csv` - All games with error analysis
- `games_with_errors_only_imb.csv` - Filtered games with only IMB errors
- `errors_imb_with_result_and_phase_player_only.csv` - Error analysis by game phase
- `phase_error_winrates.csv` - Win rates by phase and error type
- `opening_stats_by_color.csv` - Opening statistics by color

## Setup

### Quick Setup (Automated)

Run the setup script to automatically configure everything:
```bash
./setup.sh
```

### Manual Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Install Stockfish engine:**
   
   **Fedora/RHEL:**
   ```bash
   sudo dnf install stockfish
   ```
   
   **Ubuntu/Debian:**
   ```bash
   sudo apt update && sudo apt install stockfish
   ```
   
   **Arch Linux:**
   ```bash
   sudo pacman -S stockfish
   ```
   
   **macOS (with Homebrew):**
   ```bash
   brew install stockfish
   ```
   
   **Manual installation:**
   - Download from https://stockfishchess.org/download/
   - Update the `STOCKFISH_PATH` in [Clean.py](Clean.py) to point to your Stockfish executable

3. **Verify setup:**
   ```bash
   python test_setup.py
   ```

4. **Prepare your data:**
   - Place your PGN files (`MAF13-white.pgn`, `MAF13-black.pgn`) in the project directory

## Usage

1. **Analyze games for errors:**
   ```bash
   python Clean.py
   ```
   This will process your PGN files and generate error analysis data.

2. **Calculate statistics:**
   ```bash
   python Calculation.py
   ```
   Processes the error data and generates filtered datasets.

3. **Generate analytics:**
   ```bash
   python Analytics.py
   ```
   Creates analytical reports and win rate statistics.

4. **Analyze openings:**
   ```bash
   python Openings.py
   ```
   Generates opening performance statistics by color.

## Configuration

### Engine Settings (Clean.py)
- `DEPTH_BEST` - Depth for best move calculation (default: 10)
- `DEPTH_PLAYED` - Depth for played move evaluation (default: 8)
- `STOCKFISH_PATH` - Path to Stockfish executable

### Error Types
The project analyzes three types of errors:
- **Inaccuracy** - Minor suboptimal moves
- **Mistake** - More significant errors
- **Blunder** - Serious tactical/strategic errors

## Requirements

- Python 3.8+
- pandas
- python-chess
- Stockfish engine

## Notes

- Update the Stockfish path in `Clean.py` before running analysis
- The project assumes you have separate PGN files for games where you played White vs Black
- Error thresholds and analysis parameters can be adjusted in the respective Python files