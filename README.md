[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/philipwfowler/quantitative_biochemistry/HEAD)

This repository will contain all the lectures for the Quantitative Biochemistry course that is part of the Biochemistry first-year course at Oxford University. 

# Status
All lectures were recorded in 2020/1 using Panopto and split into 10-15 min segments.

# Install
This is a Python3 module; recommend you install via

`python install -e .`

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
10 October 2021
