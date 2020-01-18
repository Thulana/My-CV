# The name of the main .tex file to build.
# Other files can be included into this one.
DOCUMENT = cv
OUTPUT = .
PDF = $(OUTPUT)/$(DOCUMENT).pdf

LATEX_FLAGS = -halt-on-error -output-directory $(OUTPUT)/
LATEX = xelatex
PDFVIEWER = xdg-open

# File Types (for dependencies)
TEX = $(wildcard *.tex)
BIB = $(wildcard *.bib)
STY = $(wildcard *.sty)
CLS = $(wildcard *.cls)
BST = $(wildcard *.bst)


# TARGETS
###############################################################################

all: $(PDF)

$(OUTPUT)/%.pdf: %.tex $(STY) $(CLS) $(BIB) $(BST)
	mkdir -p $(OUTPUT)
	$(LATEX) $(LATEX_FLAGS) $<
	$(LATEX) $(LATEX_FLAGS) $< 1>/dev/null

show: all
	@ # Redirect stdout and stderr to /dev/null for silent execution
	@ (${PDFVIEWER} $(PDF) > /dev/null 2>&1 & )

### Clean
# This target cleans the temporary files generated by the tex programs
clean:
	rm -rf *.aux *.
