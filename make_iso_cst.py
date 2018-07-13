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

import argparse



#import csv, os, re
#from Bio import SeqIO

def main(pdb, outfile):
    pdb = 'RrgA.final.pdb'

    import re
    for l in open(pdb):
        if 'LINK' in l:
            break
    else:
        raise Exception('No LINK line')

    lys = int(re.search('LYS A\s*(\d+)', l).group(1))
    asx = int(re.search('AS[NPX] A\s*(\d+)', l).group(1))
    template = '''AtomPair NZ {lys}A CG {asp}A HARMONIC 1.30 0.3
    AtomPair CE {lys}A CG {asp}A HARMONIC 2.40 0.3
    AtomPair 1HZ {lys}A OD1 {asp}A HARMONIC 3.20 0.3
    Angle CE {lys}A NZ {lys}A CG {asp}A CIRCULARHARMONIC 2.08 0.2 #119 deg
    Angle NZ {lys}A CG {asp}A OD1 {asp}A CIRCULARHARMONIC 2.08 0.2
    Dihedral CE {lys}A NZ {lys}A CG {asp}A CB {asp}A CIRCULARHARMONIC 3.14159 0.2
    Dihedral 1HZ {lys}A NZ {lys}A CG {asp}A OD1 {asp}A CIRCULARHARMONIC 3.14159 0.2'''

    open(outfile,'w').write(template.format(lys=lys, asp=asx))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__description__)
    parser.add_argument("input", help="the input pdb ref file")
    parser.add_argument("output", help="the output cst file")
    parser.add_argument('--version', action='version', version=__version__)
    args = parser.parse_args()
    main(args.input, args.output)