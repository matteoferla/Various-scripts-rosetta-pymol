#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Written for python 3, not tested under 2.
"""

"""
__author__ = "Matteo Ferla. [Github](https://github.com/matteoferla)"
__email__ = "matteo.ferla@gmail.com"
__date__ = ""
__license__ = "Cite me!"
__version__ = "1.0"

import argparse

import re




def bfactorise(infile,outfile):
    structure = []
    bfactors = {}
    for l in open(infile, 'r'):
        rex = re.match('\w.*?_(\d+)', l)
        if l.find('ATOM') != -1:
            structure.append(l)
        elif rex:
            resn = l.split(' ')
            bfactors[int(rex.group(1))] = float(resn[-1])

    baseline = 0 - min(bfactors.values())

    w = open(outfile, 'w')
    for a in structure:
        print(a)
        a = ''.join(a[0:61]) + '{: >5.2f}'.format(bfactors[int(a[23:26])] + baseline) + ''.join(a[66:])
        w.write(a)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='This program gets a pdb file from Rosetta Relax and puts the per residue scores as B-factors')
    parser.add_argument("infile", help="the input pdb file from Rosetta Relax")
    parser.add_argument("outfile", help="the output pdb file")
    args = parser.parse_args()
    bfactorise(args.infile,args.outfile)