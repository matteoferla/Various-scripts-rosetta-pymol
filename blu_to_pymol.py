#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__description__ = \
    """
Script that converts a Rosetta remodel blueprint into a series of commands for Pymol to colour code so to show what has been done.
Residues that are mutated (e.g. `1 A D PIKAA G`) are coloured red, while residues nearby that are wobbled (e.g. `1 A D PIKAA A`) are coloured red.
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


# import csv, os, re
# from Bio import SeqIO

def blu(infile):
    # 1 V D PIKAA V
    # clean.
    offset = 0
    pep = []
    last = 0
    wobble = []
    mutate = []
    for line in open(infile):
        ls = line.split()
        resi = int(ls[0])
        if resi == 0:
            offset += 1
            c_resi = last + offset
        else:
            last = resi
            c_resi = resi + offset
        if ls[2] != '.':
            if ls[1] != ls[4]:
                mutation = 'mutate'
                mutate.append(str(c_resi))
            else:
                mutation = 'wobble'
                wobble.append(str(c_resi))
        else:
            mutation = 'no'

        pep.append({'resi': ls[0],
                    'c_resi': str(c_resi),
                    'resn': line[1],
                    'mutate': mutation})
    print('bg_color white')
    print('show cartoon')
    print('hide lines')
    print('color grey60, (name C*)')
    print('color yellow, (name C*) & resi ' + '+'.join(wobble))
    print('color red, (name C*) & resi ' + '+'.join(mutate))
    print('show sticks, resi ' + '+'.join(mutate))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__description__)
    parser.add_argument("input", help="the input blue file")
    parser.add_argument('--version', action='version', version=__version__)
    args = parser.parse_args()
    blu(args.input)

    '''    # 1 V D PIKAA V
    mut_flag=False
    first_mut=1
    for line in [line.split() for line in open('toSpyC2.1.blu')]:
        if line[2] != '.':
            if not mut_flag:
                mut_flag = True
                first_mut = line[0]
            if line[1] != line[4]:
                print(line[1] + line[0] + line[4])
        elif mut_flag:
            mut_flag = False'''
