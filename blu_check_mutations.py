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


#import csv, os, re
#from Bio import SeqIO


#1 V D PIKAA V
for line in [line.split() for line in open('toSpyC2.1.blu')]:
    if line[2] != '.':
        if line[1] != line[4]:
            print(line[1]+line[0]+line[4])