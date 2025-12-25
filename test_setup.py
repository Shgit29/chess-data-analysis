#!/usr/bin/env python3
"""
Test script to verify the Chess Data Analysis Project setup
"""

import sys
import subprocess
from pathlib import Path

def test_python_packages():
    """Test if required Python packages are available"""
    print("🐍 Testing Python packages...")
    
    try:
        import pandas
        print(f"✅ pandas {pandas.__version__}")
    except ImportError:
        print("❌ pandas not installed")
        return False
    
    try:
        import chess
        print(f"✅ chess {chess.__version__}")
    except ImportError:
        print("❌ chess not installed")
        return False
    
    return True

def test_stockfish():
    """Test if Stockfish engine is available"""
    print("\n♛ Testing Stockfish engine...")
    
    # Common Stockfish paths
    stockfish_paths = [
        "/usr/bin/stockfish",      # Fedora/Arch
        "/usr/games/stockfish",    # Ubuntu/Debian
        "/opt/homebrew/bin/stockfish",  # macOS Homebrew
        "stockfish"                # In PATH
    ]
    
    for path in stockfish_paths:
        try:
            result = subprocess.run([path, "--help"], 
                                  capture_output=True, 
                                  text=True, 
                                  timeout=5)
            if result.returncode == 0:
                print(f"✅ Stockfish found at: {path}")
                return True, path
        except (subprocess.TimeoutExpired, FileNotFoundError, OSError):
            continue
    
    print("❌ Stockfish not found. Please install it:")
    print("   Fedora: sudo dnf install stockfish")
    print("   Ubuntu: sudo apt install stockfish")
    print("   macOS:  brew install stockfish")
    return False, None

def test_project_files():
    """Test if required project files exist"""
    print("\n📁 Testing project files...")
    
    required_files = [
        "Clean.py",
        "Calculation.py", 
        "Analytics.py",
        "Openings.py",
        "requirements.txt",
        "README.md"
    ]
    
    all_present = True
    for file in required_files:
        if Path(file).exists():
            print(f"✅ {file}")
        else:
            print(f"❌ {file} missing")
            all_present = False
    
    return all_present

def test_chess_functionality():
    """Test basic chess functionality"""
    print("\n♟️  Testing chess functionality...")
    
    try:
        import chess
        import chess.engine
        
        # Test basic chess operations
        board = chess.Board()
        print(f"✅ Chess board created: {board.fen()}")
        
        # Test move parsing
        move = chess.Move.from_uci("e2e4")
        board.push(move)
        print(f"✅ Move executed: {move}")
        
        return True
    except Exception as e:
        print(f"❌ Chess functionality error: {e}")
        return False

def main():
    """Run all tests"""
    print("🔧 Chess Data Analysis Project - Setup Verification\n")
    
    tests_passed = 0
    total_tests = 4
    
    # Test Python packages
    if test_python_packages():
        tests_passed += 1
    
    # Test Stockfish
    stockfish_ok, stockfish_path = test_stockfish()
    if stockfish_ok:
        tests_passed += 1
    
    # Test project files
    if test_project_files():
        tests_passed += 1
    
    # Test chess functionality
    if test_chess_functionality():
        tests_passed += 1
    
    # Summary
    print(f"\n📊 Test Results: {tests_passed}/{total_tests} tests passed")
    
    if tests_passed == total_tests:
        print("\n🎉 All tests passed! Your setup is ready.")
        print("\nNext steps:")
        print("1. Place your PGN files (MAF13-white.pgn, MAF13-black.pgn) in this directory")
        print("2. Run: python Clean.py")
    else:
        print("\n⚠️  Some tests failed. Please check the output above and fix the issues.")
        if not stockfish_ok:
            print("   Install Stockfish first, then run this test again.")
    
    return tests_passed == total_tests

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)