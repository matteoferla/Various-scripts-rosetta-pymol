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

import argparse, csv
from pprint import PrettyPrinter
from collections import defaultdict
pp = PrettyPrinter()


#import csv, os, re
#from Bio import SeqIO

def renumber(infile, outfile, iso, delete=[], insert=None):
    first_delete=[]
    last_delete=[]
    if delete:
        for d in delete:
            first_delete.append(int(d.split(':')[0]))
            last_delete.append(int(d.split(':')[1]))
    if insert:
        (first_insert, insert_amount)=[int(x) for x in insert.split('+')]
    else:
        (first_insert, insert_amount)= None, None

    w=csv.writer(open(outfile,'w'))
    w.writerow('resi from_resn to_resn average_ddG average_total_energy'.split())

    mutdex=defaultdict(list)
    for line in open(infile):
        parts=line.split()
        if parts[1][0] != 'A':
            continue
        resi=int(parts[2][3:-1])
        if resi and resi > 0 and resi < 1e3:
            mutdex[resi].append([parts[2][2],parts[2][-1], parts[3], parts[4]]) # resi from_resn to_resn average_ddG average_total_energy

    def write_rows(resi, mutdex):
        returndex = []
        for r in 'A C D E F G H I K L M N P Q R S T V W Y'.split():
            if r == mutdex[resi][0][0]:
                returndex.append([resi + current_offset, mutdex[resi][0][0], r, 0, 'SELF'])
            else:
                for data in mutdex[resi]:
                    if data[1] == r:
                        returndex.append([resi + current_offset] + data)
                        break
                else:
                    print('Missing entry', mutdex[resi][0][0], resi, r)
                    returndex.append([resi + current_offset, mutdex[resi][0][0], r, 'BAD', 'BAD'])
        return returndex

    delete_flag = False
    current_offset = 0
    for resi in range(1,max(mutdex.keys())+1):
        if delete_flag == True or resi in first_delete:
            if resi in last_delete: # last one to skip...
                delete_flag = False
            else:
                delete_flag = True
            current_offset -= 1
            print('Deleting...', resi, mutdex[resi][0][0])
            continue
        elif resi == first_insert:
            w.writerows(write_rows(resi, mutdex))
            for n in range(insert_amount):
                current_offset += 1
                for r in 'A C D E F G H I K L M N P Q R S T V W Y'.split():
                    w.writerow([resi+current_offset,'X',r,'NA','NA'])
        elif not resi in mutdex: # no offsetting... just filling
            for r in 'A C D E F G H I K L M N P Q R S T V W Y'.split():
                w.writerow([resi + current_offset, 'X', r, 'NA', 'NA'])
        elif resi in iso:    # no offsetting... just skipping
            print('Removing iso...', resi, mutdex[resi][0][0])
            continue #skip
        else:
            w.writerows(write_rows(resi, mutdex))

renumber('dog-unreact_scores.txt','dog.no.csv',iso=[9,70,121])
renumber('dog-whole_scores.txt','dog.iso.csv',iso=[9,70,121])
renumber('dog-intermediate_scores.txt','dog.trans.csv',iso=[9,70,121])

exit()
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__description__)
    parser.add_argument("input", help="the input file")
    parser.add_argument("output", help="the output file")
    parser.add_argument('-delete', nargs='+', help="residue range with colon, 1:10 will delete 1 to 10 inclusive and fix subsequent numbering")
    parser.add_argument('-insert', help="residue number plus number of residues to insert, 20+3 will fix subsequent as it one had inserted 3 residues after position 20.")
    parser.add_argument('-iso', nargs=3, type=int, help="The three isopeptide residues indices spaced out")
    parser.add_argument('--version', action='version', version=__version__)
    args = parser.parse_args()
    renumber(args.input, args.output, args.delete, args.insert, args.iso)

'''print('wt iso')
renumber('2x5p.iso.scan.tsv','2x5p.iso.scan.csv',iso=[31,77,117],insert='110+6')
print('003 no')
renumber('scanner.Spy003.no.scan.tsv','Spy003.no.scan.csv',iso=[34,80,135],delete=['1:3','117:125'])
print('003 inv')
renumber('Spy003.inv.scan.tsv','Spy003.inv.scan.csv',iso=[34,80,135], delete=['1:3','117:125'])
print('003 flip')
renumber('Spy003.flip.scan.tsv','Spy003.flip.scan.csv',iso=[34,80,135], delete=['1:3','117:125'])
print('003 cut')
renumber('Spy003.cut.scan.tsv','Spy003.cut.scan.csv',iso=[34,80,135], delete=['1:3','117:125'])
print('003 iso')
renumber('Spy003.iso.scan.tsv','Spy003.iso.scan.csv',iso=[34,80,135], delete=['1:3','117:125'])'''
