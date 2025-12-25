# Configuration file for Chess Data Analysis Project
# Copy this file to config.py and modify as needed

# Stockfish Engine Configuration
STOCKFISH_PATHS = {
    "fedora": "/usr/bin/stockfish",
    "ubuntu": "/usr/games/stockfish", 
    "debian": "/usr/games/stockfish",
    "arch": "/usr/bin/stockfish",
    "macos": "/opt/homebrew/bin/stockfish",
    "windows": "C:/path/to/stockfish.exe",
    "custom": "/your/custom/path/to/stockfish"
}

# Analysis Configuration
ANALYSIS_CONFIG = {
    "DEPTH_BEST": 10,        # Depth for calculating best move
    "DEPTH_PLAYED": 8,       # Depth for evaluating played move
    "PROGRESS_EVERY": 10,    # Update progress every N moves
    "ENGINE_THREADS": 4,     # Number of threads for Stockfish
    "ENGINE_HASH": 512       # Hash size in MB for Stockfish
}

# Error Thresholds (centipawns)
ERROR_THRESHOLDS = {
    "inaccuracy_min": 50,    # Minimum centipawns for inaccuracy
    "mistake_min": 100,      # Minimum centipawns for mistake  
    "blunder_min": 300       # Minimum centipawns for blunder
}

# File Paths
FILE_PATHS = {
    "white_pgn": "MAF13-white.pgn",
    "black_pgn": "MAF13-black.pgn",
    "games_raw": "games_raw.csv",
    "games_with_errors": "games_with_errors.csv",
    "errors_imb_only": "games_with_errors_only_imb.csv",
    "phase_analysis": "errors_imb_with_result_and_phase_player_only.csv",
    "opening_stats": "opening_stats_by_color.csv"
}