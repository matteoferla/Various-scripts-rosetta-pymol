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

import argparse, re
from pprint import PrettyPrinter

pp = PrettyPrinter()


#import csv, os, re
#from Bio import SeqIO

def main(infile, nresi, nresn):
    pdb = list(open(infile, 'r').readlines())
    out=''
    for line in pdb:
        if line.find('LINK') == 0:
            out+=line
        elif line.find('ATOM') == 0 or line.find('HETATM') == 0:
            rex = re.search('\w+M\s*(\d+)\s*(\w+)\s*(\w+)\s*(\d+)(.*)', line)
            resi = rex.group(4)
            resn = rex.group(3)
            name = rex.group(2)
            if resi == nresi:
                out+=line.replace(resn,nresn)
            else:
                out += line
    return out


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__description__)
    parser.add_argument("input", help="the input pdb file")
    parser.add_argument('resi', help='the residue number')
    parser.add_argument('resn', help='the three letter code of the new residue number')
    parser.add_argument('--version', action='version', version=__version__)
    args = parser.parse_args()
    print(main(args.input, args.resi,args.resn))