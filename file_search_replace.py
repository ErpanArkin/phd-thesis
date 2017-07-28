#!/usr/bin/env python3
import fileinput
import numpy as np

"""
replace the first column text with the second column one in file bib_key_replace
"""

with open('bib_key_replace','r') as f:
    for le in f:
        with fileinput.FileInput(['./Chapter6/chapter6.tex','./Chapter4/chapter4.tex','./Chapter5/chapter5.tex',
        './Chapter3/chapter3.tex','./Chapter2/chapter2.tex','./Chapter1/chapter1.tex'],inplace=True) as file:
             for line in file:
                 print(line.replace(le.split()[0], le.split()[1]), end='')
f.closed