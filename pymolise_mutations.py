#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__description__ = \
    """
Given a list of mutations gives a pymol set of comands to show them.

    $ python3 pymolise_mutations.py I34E M69Y
    hide all
    show cartoon
    set cartoon_transparency, 0.5
    select mutants, resi 34+69
    show sticks, mutants  & name C*
    color tv_red, sticks

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

def main(mutations):
    print('hide all')
    print('show cartoon')
    print('set cartoon_transparency, 0.5')
    print('select mutants, resi '+'+'.join([re.search('\w(\d+)\w',m).group(1) for m in mutations]))
    print('show sticks, mutants')
    print('color tv_red, mutants & name C*')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__description__)
    parser.add_argument('--version', action='version', version=__version__)
    parser.add_argument("mutations", nargs='+', help="the list of mutations, eg. C2S")
    args = parser.parse_args()
    main(args.mutations)