.PHONY: help html latex clean all setup

help:
	@echo "CV Generation System"
	@echo "===================="
	@echo ""
	@echo "Available commands:"
	@echo "  make setup   - Setup virtual environment and dependencies"
	@echo "  make html    - Generate ATS-friendly HTML resume"
	@echo "  make latex   - Generate LaTeX PDF (if you have pdflatex)"
	@echo "  make all     - Generate both versions"
	@echo "  make clean   - Remove generated files"
	@echo "  make view    - Open HTML in browser"
	@echo ""

setup:
	@./setup.sh

html:
	@./generate.sh

latex:
	@echo "Generating LaTeX PDF..."
	@if command -v pdflatex >/dev/null 2>&1; then \
		pdflatex cv.tex; \
		echo "✓ Done! Check cv.pdf"; \
	else \
		echo "❌ pdflatex not found. Install TeX Live or MiKTeX"; \
	fi

all: html latex

clean:
	@echo "Cleaning generated files..."
	rm -f cv-output.html
	rm -f cv.pdf cv.aux cv.log cv.out
	@echo "✓ Cleaned!"

view:
	@echo "Opening HTML in browser..."
	@if command -v open >/dev/null 2>&1; then \
		open cv-output.html; \
	elif command -v xdg-open >/dev/null 2>&1; then \
		xdg-open cv-output.html; \
	else \
		echo "Please open cv-output.html manually"; \
	fi
