[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/philipwfowler/quantitative_biochemistry/master)


This repository will contain all the lectures for the Quantitative Biochemistry course that is part of the Biochemistry first-year course at Oxford University. 

# Status
Lectures 1-4 have been recorded. 

# Install
This is a Python3 module; recommend you install via

`python setup.py develop --user`

This will put the script `qb-modify-latex.py` into your `$PATH` which you will need below.

# Pre-requisities

* matplotlib
* numpy
* jupyter-lab 
* working LaTeX installation that includes `pdflatex`

# Convert a lecture.ipynb to a PDF via LaTeX

```
$ cd quantitative_biochemistry/
$ jupyter-nbconvert --to latex Lecture\ 01\ -\ Introduction.ipynb
$ qb-modify-latex.py --latex Lecture\ 01\ -\ Introduction.tex > L01.tex
$ pdflatex L01.tex
$ open L01.pdf 
```

Philip W Fowler
19 October 2020
