#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__description__ = \
    """
Rosetta spits out PBD files but not good old fashioned genetic mutation lists. This fixes things.
It recognises insertions and deletions, but it reads the first chain only... which is fine as waters and often other chains get stripped anyway.
NB. Written for python 3, not tested under 2.
"""
__author__ = "Matteo Ferla. [Github](https://github.com/matteoferla)"
__email__ = "matteo.ferla@gmail.com"
__date__ = ""
__license__ = "Cite me!"
__version__ = "1.0"

import argparse
from Bio import PDB
from Bio import pairwise2

def PDB_seq_comparer(ref, mutants):
    ppar=PDB.PDBParser()
    ppb = PDB.CaPPBuilder()
    structure=ppar.get_structure('ref', ref)[0]
    rseq=ppb.build_peptides(structure)[0].get_sequence()
    for mut in mutants:
        structure = ppar.get_structure('mut', mut)[0]
        mseq = ppb.build_peptides(structure)[0].get_sequence()
        a=pairwise2.align.globalxx(str(rseq),str(mseq))[0]
        offset=0
        mlist=[]
        for i in range(len(a[0])):
            #print(a[0][i], a[1][i])
            if a[0][i] == '-':
                offset-=1
                mlist.append('ins_' + str(i+offset) + a[1][i])
            elif a[1][i] == '-':
                offset+=1
                mlist.append('del_' + a[0][i]+str(i+offset))
            elif a[0][i] != a[1][i]:
                mlist.append(a[0][i]+str(i+offset)+a[1][i])
        print(mut+'\t'+' '.join(mlist))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__description__)
    parser.add_argument("ref", help="the ref PDB file")
    parser.add_argument("mutants", help="the mutant pbd files", nargs='*')
    parser.add_argument('--version', action='version', version=__version__)
    args = parser.parse_args()
    PDB_seq_comparer(args.ref, args.mutants)
