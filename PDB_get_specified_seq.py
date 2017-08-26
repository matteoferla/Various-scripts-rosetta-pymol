#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__description__ = \
    """
This script is a variant of sorts of `PDB_seq_comparer.py` in which the user specifies the start and stop positions to count the number of times residues appear there.
This script was written to get the consensus of rosetta remodel pdbs.
NB. Written for python 3, not tested under 2.
"""
__author__ = "Matteo Ferla. [Github](https://github.com/matteoferla)"
__email__ = "matteo.ferla@gmail.com"
__date__ = ""
__license__ = "Cite me!"
__version__ = "1.0"

import argparse
from pprint import PrettyPrinter

pp = PrettyPrinter()
from Bio import PDB
from Bio import pairwise2
from collections import Counter


#import csv, os, re
#from Bio import SeqIO

def PDB_seq_comparer(ref, mutants, start,stop):
    print('pos\t'+'\t'.join([str(i) for i in range(start+1,stop+1)]))
    ppar=PDB.PDBParser()
    ppb = PDB.CaPPBuilder()
    structure=ppar.get_structure('ref', ref)[0]
    rseq=ppb.build_peptides(structure)[0].get_sequence()
    print('wt'+'\t'+'\t'.join([r for r in rseq[start:stop]]))
    mutdex=[Counter() for i in range(start,stop)]
    for mut in mutants:
        structure = ppar.get_structure('mut', mut)[0]
        mseq = ppb.build_peptides(structure)[0].get_sequence()
        print(mut + '\t' + '\t'.join([r for r in mseq[start:stop]]))
        for i in range(stop-start):
            mutdex[i].update(mseq[i+start])
    pp.pprint(mutdex)




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__description__)
    parser.add_argument("ref", help="the ref PDB file")
    parser.add_argument("start", help="the start position")
    parser.add_argument("stop", help="the stop position")
    parser.add_argument("mutants", help="the mutant pbd files", nargs='*')
    parser.add_argument('--version', action='version', version=__version__)
    args = parser.parse_args()
    PDB_seq_comparer(args.ref, args.mutants, int(args.start)-1, int(args.stop))