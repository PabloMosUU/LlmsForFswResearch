all: withnotes withoutnotes movepdf
	
withnotes: slides.tex
	lualatex -interaction=nonstopmode -halt-on-error -jobname presentation-notes '\providecommand\shownotes{1}\input{slides}'
	lualatex -interaction=nonstopmode -halt-on-error -jobname presentation-notes '\providecommand\shownotes{1}\input{slides}'

withoutnotes: slides.tex
	lualatex -interaction=nonstopmode -halt-on-error -jobname presentation-nonotes '\providecommand\shownotes{0}\input{slides}'
	lualatex -interaction=nonstopmode -halt-on-error -jobname presentation-nonotes '\providecommand\shownotes{0}\input{slides}'

movepdf:
	mkdir -p _site/slides
	cp presentation-notes.pdf _site/slides/
	cp presentation-nonotes.pdf _site/slides/
	rm -f *.aux *.log *.nav *.out *.snm *.toc

clean:
	rm -f *.aux *.log *.nav *.out *.snm *.toc
	rm -f _site/slides/*.pdf
