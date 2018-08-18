#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Written for python 3, not tested under 2.
"""
Give a single-headed comma-separated table where the two rows are like:
master,unreact,iso,dddG
A-K1A,2.595,2.636,0.041
it will get all the cases where the destabilation is less than threshold for iso and maps to bfactor the best change in energy.
red = high = destabilising iso
blue = low = stabilising iso.
"""
__author__ = "Matteo Ferla. [Github](https://github.com/matteoferla)"
__email__ = "matteo.ferla@gmail.com"
__date__ = ""
__license__ = "Cite me!"
__version__ = "1.0"

import argparse

import re, csv
from collections import defaultdict




def bfactorise(infile,table,outfile, threshold_iso=5, threshold_unreact=50):
    structure = []
    bfactors = {}
    w = open(outfile, 'w')
    read=csv.reader(open(table,'r'),delimiter=',')
    next(read)
    aadex=defaultdict(list)
    for row in read:
        resi=re.search('(\d+)',row[0]).group(1)
        if float(row[2]) < threshold_iso and float(row[1]) < threshold_unreact:
            aadex[resi].append(float(row[3]))
    aamindex={int(k): min(aadex[k]) for k in aadex}

    baseline=min(aamindex.values())
    for k in range(1,max(aamindex.keys())+1):
        if k not in aamindex:
            aamindex[k]=-baseline
        aamindex[k]=aamindex[k]-baseline
        if aamindex[k]>-baseline:
            aamindex[k]=-baseline

    for l in open(infile, 'r'):
        if l.find('LINK') != -1:
            w.write(l)
        elif l.find('ATOM') != -1:
            w.write(''.join(l[0:61]) + '{: >5.2f}'.format(aamindex[int(l[23:26])]) + ''.join(l[66:]))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='This program gets a pdb file from Rosetta Relax and puts the per residue scores as B-factors')
    parser.add_argument("infile", help="the input pdb file")
    parser.add_argument("table", help="the input table file with first column A-XNY and four the ∆∆∆G")
    parser.add_argument("outfile", help="the output pdb file")
    args = parser.parse_args()
    bfactorise(args.infile,args.table,args.outfile)