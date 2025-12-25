#!/bin/bash

echo "🔧 Compiling LaTeX report to PDF..."

# Check if pdflatex is available
if ! command -v pdflatex &> /dev/null; then
    echo "❌ Error: pdflatex not found. Please install LaTeX distribution:"
    echo "   Fedora: sudo dnf install texlive-latex texlive-latex-extra"
    echo "   Ubuntu: sudo apt install texlive-latex-base texlive-latex-extra"
    echo "   macOS: brew install --cask mactex"
    exit 1
fi

# Clean previous compilation files
echo "🧹 Cleaning previous compilation files..."
rm -f report.aux report.log report.toc report.out report.fdb_latexmk report.fls

# Compile LaTeX document (run twice for cross-references)
echo "📄 First compilation pass..."
pdflatex -interaction=nonstopmode report.tex > /dev/null 2>&1

echo "📄 Second compilation pass (for cross-references)..."
pdflatex -interaction=nonstopmode report.tex > /dev/null 2>&1

# Check if PDF was created successfully
if [ -f "report.pdf" ]; then
    echo "✅ Report compiled successfully: report.pdf"
    echo ""
    echo "📊 Report statistics:"
    echo "   File size: $(du -h report.pdf | cut -f1)"
    echo "   Pages: $(pdfinfo report.pdf 2>/dev/null | grep Pages | awk '{print $2}' || echo 'Unknown')"
    echo ""
    echo "💡 To view the report:"
    echo "   Linux: xdg-open report.pdf"
    echo "   macOS: open report.pdf"
    echo "   Windows: start report.pdf"
else
    echo "❌ Error: Failed to compile report. Check LaTeX installation and syntax."
    echo "   See report.log for details"
    exit 1
fi

# Clean auxiliary files but keep PDF
echo "🧹 Cleaning auxiliary files..."
rm -f report.aux report.log report.toc report.out report.fdb_latexmk report.fls

echo "🎉 Report compilation complete!"