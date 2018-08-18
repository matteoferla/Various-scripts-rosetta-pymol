#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__description__ = \
    """
Given the two isopeptide residues (eg. K34 D125 it spits out a cst string...
NB. Written for python 3, not tested under 2.
"""
__author__ = "Matteo Ferla. [Github](https://github.com/matteoferla)"
__email__ = "matteo.ferla@gmail.com"
__date__ = ""
__license__ = "Cite me!"
__version__ = "1.0"

import argparse


def id_resi(resi1,resi2):
    """
    returns (lys,asx) tuple from two residues resi1, resi2, one of which lys, the other asp/asn
    :param resi1: single letter + number e.g. D12
    :param resi2: single letter + number e.g. K12
    :return:
    """
    if resi1[0]=='K':
        lys=resi1
        asx=resi2
    elif resi2[0] == 'K':
        lys=resi2
        asx = resi1
    else:
        raise ValueError('neither residue is K')
    assert asx[0] in ('D','N'), 'neither residue is N/D'
    return lys,asx

def isomaker(resi1, resi2):
    """
    Given the two isopeptide residues (eg. K34 D125 it spits out a cst string
    :param resi1:
    :param resi2:
    :return: String
    """
    template='''AtomPair NZ {K}A CG {D}A HARMONIC 1.30 0.3
AtomPair CE {K}A CG {D}A HARMONIC 2.40 0.3
AtomPair 1HZ {K}A OD1 {D}A HARMONIC 3.20 0.3
Angle CE {K}A NZ {K}A CG {D}A CIRCULARHARMONIC 2.08 0.2 #119 deg
Angle NZ {K}A CG {D}A OD1 {D}A CIRCULARHARMONIC 2.08 0.2
Dihedral CE {K}A NZ {K}A CG {D}A CB {D}A CIRCULARHARMONIC 3.14159 0.2
Dihedral 1HZ {K}A NZ {K}A CG {D}A OD1 {D}A CIRCULARHARMONIC 3.14159 0.2'''
    #identify residues
    lys,asx=id_resi(resi1,resi2)
    #format & return
    return template.format(K=lys, D=asx)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__description__)
    parser.add_argument("resi1", help="one residue")
    parser.add_argument("resi2", help="another residue")
    parser.add_argument('--version', action='version', version=__version__)
    args = parser.parse_args()
    print(isomaker(args.resi1, args.resi2))