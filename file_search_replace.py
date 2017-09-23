#!/usr/bin/env python3
import fileinput
import numpy as np

"""
replace the first column text with the second column one in file bib_key_replace
"""

with open('bib_key_replace','r') as f:
    for le in f:
        with fileinput.FileInput(['./Chapter1/chapter1.tex'],inplace=True) as file:
             for line in file:
                 if le.split()[0] is in line:
                     input_var = input("Enter something: ")
                     if input_var == 't':
                      print(line.replace(le.split()[0], le.split()[1]), end='')
                     else:
                      continue
f.closed