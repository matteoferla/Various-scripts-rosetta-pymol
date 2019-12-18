# Fluorescein
Rosetta params for thiol conjugated with Fluorescein-5-maleimide.

## Details
Fluorescein-maleimide, once reacted with a thio is fluorescein-succinimide. When the anhydride ring is hydrolysed it is a fluorescein-succinamate. The name FLS and FSO are completely arbitrary.

## Making of
The ligand (fluorescein-succinimide or fluorescein-succinamate) was manually generate with a combination of PubChem, python rdkit and ChemDraw Ultra editing to generate SMILES strings that were converted into a 3D structure using https://cactus.nci.nih.gov/cgi-bin/translate.tcl. Gaussian was not used to optimise the structures.
These were made as thiol-reacted ligands, which after parameterisation with the script `molfile_to_params.py`.
These were edited to alter the sulfur (`BOND` to `CONNECT`) and replace it with a connector `CONN1`.
The trick to make it work is make an old school cst and use the depracated `ligand_dock` application.

## Usage
Relax your protein with all the missing loops and stuff fixed —so if Rosetta gets grumpy you know it is this ligand.    
Do the following in PyMol:     

	#Get your protein and ligand (obs. you have to have cd'ed in the folder)
	load protein.pdb
	load FLS_0001.pdb
	#Align to cysteine (assumes a single cysteine)
	pair_fit resn FLS & name S1, resn cys & name SG, resn FLS & name C1, resn cys & name HG
	#Remove the sulfur of the ligand and the HG proton from the cysteine.
	remove resn FLS & name S1
	remove resn CYS & name HG
	select lig, resn FLS
	#The chain does not need to match, but it does have to be consistent.
	alter lig, chain='A'
	alter lig, resi='n' #where n is the last chain.
	alter resn CYS, resn='CYD'
	sort
	#save
	save myprotein-FLS.pdb,all

In the above the HG atom will cause trouble and cysteine needs to be deprotonated.

Ammend the PDB file to contain: `REMARK 666 MATCH TEMPLATE A CYS  XX MATCH MOTIF A FLS   YY  1  1 `
where XX is the residue id of cysteine and YY of the FLS.     
NB. A CONECT line can be added but Rosetta does not care.     
Now you can dock it. I used the now depracated, but still ligand_dock due to the constraints —the new one misbehaves!  

	$ROSETTA/ligand_dock.$ROSETTAEXT -database $ROSETTADB -ex1 -ex1aro -ex2 -extrachi_cutoff 1 -no_optH false -extra_res_fa yyy.params -enzdes:cstfile yyy-bond.cst  -docking -minimize_ligand -harmonic_torsions 10 -improve_orientation 1000 -out:pdb 1 -out:nstruct 100 -out:level 300 -s xxx-yyy.pdb;

Where `yyy` is either FLS or FSO and `xxx` is your protein.
	
	


