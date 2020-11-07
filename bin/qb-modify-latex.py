#! /usr/bin/env python

import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--latex",required=True,help="the path to a LaTeX file produced by nbconvert")
    options = parser.parse_args()

    keep_line =True
    in_callout={}
    for callout_text in ["Common misconception:", "Tip:","For you:",'Thought:']:
        in_callout[callout_text]=False

    callout_colour={}
    callout_colour['For you:']='green'
    callout_colour['Common misconception:']='red'
    callout_colour['Tip:']='blue'
    callout_colour['Thought:']='orange'

    with open(options.latex,'r') as INPUT:
        for line in INPUT:
            if "begin{tcolorbox}" in line:
                keep_line=False

            if "section{" in line:
                line=line.replace('section{','section*{')

            if "begin{document}" in line:
                line+="\n\date{}"


            for callout_text in ["Common misconception:", "Tip:","For you:","Thought:"]:
                search_result=line.find(callout_text)
                if search_result!=-1:
                    in_callout[callout_text]=True
                    keep_line=False
                    content=line[search_result+len(callout_text):]
                    header="\\begin{tcolorbox}[title="+callout_text+", colback="+callout_colour[callout_text]+"!5!white,colframe="+callout_colour[callout_text]+"!75!black]\n"
                    header+="\\begin{minipage}{0.15\linewidth}"
                    if callout_text in ['For you:']:
                        header+="\includegraphics{images/pointing-finger.png}\n"
                    elif callout_text=='Tip:':
                        header+="\includegraphics{images/tick.png}\n"
                    elif callout_text=='Thought:':
                        header+="\includegraphics{images/thinking-face.png}\n"
                    else:
                        header+="\includegraphics{images/curtis.jpg}\n"
                    header+='''\end{minipage}
\\begin{minipage}{0.75\linewidth}
'''
                    footer='''\end{minipage}
\end{tcolorbox}'''


                elif in_callout[callout_text]:
                    content+=line
                    if line=='\n':
                        line=header+content+footer+"\n"
                        keep_line=True
                        in_callout[callout_text]=False

            if "0.9\\linewidth" in line:
                line=line.replace("0.9\\linewidth","0.75\\linewidth")

            if "0.9\\paperheight" in line:
                line=line.replace("0.9\\paperheight","0.5\\paperheight")

            if keep_line:
                print(line.rstrip())
            elif "end{tcolorbox}" in line:
                keep_line=True
