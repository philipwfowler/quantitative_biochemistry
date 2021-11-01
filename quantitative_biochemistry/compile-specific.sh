#! /bin/bash
i=$1
#for i in `ls Lecture-$0*.ipynb`; do
filename=${i%.*}
echo $filename
jupyter-nbconvert-3.8 --to latex ${filename}.ipynb
mv ${filename}.tex foo.tex
python3 ../bin/qb-modify-latex.py --latex foo.tex > ${filename}.tex
pdflatex ${filename}.tex
#done;
    
rm foo.tex
rm Lecture*.out
rm Lecture*.aux
rm Lecture*.log

