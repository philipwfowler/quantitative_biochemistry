#! /bin/bash

for i in `ls Lecture-*.ipynb`; do
    filename=${i%.*}
    jupyter-nbconvert-3.10 --to latex ${filename}.ipynb
    mv ${filename}.tex foo.tex
    qb-modify-latex.py --latex foo.tex > ${filename}.tex
    pdflatex ${filename}.tex
done;
    
rm foo.tex
rm Lecture*.out
rm Lecture*.aux
rm Lecture*.log

