all: authors.tex pprint tex

tex:
	pdflatex -shell-escape --halt-on-error paper.tex
	bibtex paper.aux
	pdflatex -shell-escape --halt-on-error paper.tex
	pdflatex -shell-escape --halt-on-error paper.tex

authors.tex: authors/list_latex.py authors/authors.json
	cd authors; ./list_latex.py

pprint:
	xelatex --halt-on-error pprint.tex

test:
	python test-paper.py

clean:
	(rm -rf *.ps *.log *.dvi *.aux *.*% *.lof *.lop *.lot *.toc *.idx *.ilg *.ind *.bbl *.blg *.cpt)

