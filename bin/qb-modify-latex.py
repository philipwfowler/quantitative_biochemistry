#! /usr/bin/env python

import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--latex_file",required=True,help="the path to a LaTeX file produced by nbconvert")
    options = parser.parse_args()

    keep_line =True

    with open(options.latex_file,'r') as INPUT:
        for line in INPUT:
            if "begin{tcolorbox}" in line:
                keep_line=False

            if "section{" in line:
                line=line.replace('section{','section*{')

            if "begin{document}" in line:
                line+="\n\date{}"

            if "0.9\\linewidth" in line:
                line=line.replace("0.9\\linewidth","0.75\\linewidth")

            if "0.9\\paperheight" in line:
                line=line.replace("0.9\\paperheight","0.5\\paperheight")

            if keep_line:
                print(line.rstrip())
            elif "end{tcolorbox}" in line:
                keep_line=True
