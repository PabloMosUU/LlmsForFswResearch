all: presentation-notes.pdf presentation-nonotes.pdf clean

presentation-notes.pdf: slides.tex
	lualatex -interaction=nonstopmode -halt-on-error -jobname presentation-notes '\providecommand\shownotes{1}\input{slides}'
	lualatex -interaction=nonstopmode -halt-on-error -jobname presentation-notes '\providecommand\shownotes{1}\input{slides}'

presentation-nonotes.pdf: slides.tex
	lualatex -interaction=nonstopmode -halt-on-error -jobname presentation-nonotes '\providecommand\shownotes{0}\input{slides}'
	lualatex -interaction=nonstopmode -halt-on-error -jobname presentation-nonotes '\providecommand\shownotes{0}\input{slides}'

clean:
	rm -f *.aux *.log *.nav *.out *.snm *.toc
