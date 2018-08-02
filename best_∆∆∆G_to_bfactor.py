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
        # label fa_atr fa_rep fa_sol fa_intra_rep fa_elec pro_close hbond_sr_bb hbond_lr_bb hbond_bb_sc hbond_sc dslf_fa13 rama omega fa_dun p_aa_pp yhh_planarity ref total
        # LEU_2 -3.50043 0.1252 1.55802 0.00859 0.08156 0 0 0 0 0 0 -0.19676 0.00608 0.08399 -0.20463 0 0.76113 -1.27727
        rex = re.match('\w.*_(\d+)', l)
        if l.find('ATOM') != -1 or l.find('LINK') != -1:
            structure.append(l)
        elif rex:
            resn = l.split(' ')
            bfactors[int(rex.group(1))] = float(resn[3])

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