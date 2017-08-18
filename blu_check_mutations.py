#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__description__ = \
    """

NB. Written for python 3, not tested under 2.
"""
__author__ = "Matteo Ferla. [Github](https://github.com/matteoferla)"
__email__ = "matteo.ferla@gmail.com"
__date__ = ""
__license__ = "Cite me!"
__version__ = "1.0"

from pprint import PrettyPrinter

pp = PrettyPrinter()

import argparse
#import csv, os, re
#from Bio import SeqIO

def blu(infile):
    for line in [line.split() for line in open(infile)]:
        if line[2] != '.':
            if line[3] != 'PIKAA' or line[3] != 'NATAA':
                print(line[1]+line[0]+' '+line[3])
            if line[3] == 'PIKAA' and line[1] != line[4]:
                print(line[1]+line[0]+line[4])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__description__)
    parser.add_argument("input", help="the input blue file")
    parser.add_argument('--version', action='version', version=__version__)
    args = parser.parse_args()
    blu(args.input)
