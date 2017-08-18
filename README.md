# rosetta-pymol
scripts for Rosetta and PyMol stuff

## blu_to_pymol.py
Script that converts a Rosetta remodel blueprint into a series of commands for Pymol to colour code so to show what has been done.
Residues that are mutated (e.g. `1 A D PIKAA G`) are coloured red, while residues nearby that are wobbled (e.g. `1 A D PIKAA A`) are coloured red and shown as sticks.
It tollerates insertions, but not deletions.
The result is somethink like this:

    bg_color white
    show cartoon
    hide lines
    color grey60, (name C*)
    color yellow, (name C*) & resi 1+3+4+5+6+7+9+10+11+12+14+15+16+17+18+20+21+22+23+24+35+36+38+39+60+61+63+64+81+82+83+84+85+86+87+88+90+96+97+98+107+109+110+111+112+124+130
    color red, (name C*) & resi 2+8+13+19+37+62+89+108+113+114+115+116+117+118+119+120+121+122+123+131+132+133+134+135
    show sticks, resi 2+8+13+19+37+62+89+108+113+114+115+116+117+118+119+120+121+122+123+131+132+133+134+135

## blu_check_mutations.py
Simple script for sanity check of blueprint file: list the mutations present.

## PDB_to_mutlist.py
Rosetta spits out PBD files but not good old fashioned genetic mutation lists (_e.g._ A34T). This fixes things. It accepts the reference PDB and the list of mutant PDB and prints to the terminal the name and the mutations present.
It recognises insertions and deletions.
However, t reads the first chain only... which is fine as waters and often other chains get stripped anyway.

## relax_score_to_bfactor.py
Ehm... Rosetta PDB files have a per amino acid score at the end, this script makes the score become the B-factor. Please note that bad score does not mean wobbly (_i.e._ blurry on difraction pattern) but more unhappy. I cannot say what other parameters are useful as to be honest I never look at them.
