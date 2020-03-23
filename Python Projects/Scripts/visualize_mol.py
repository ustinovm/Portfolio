#!/usr/bin/python3
import subprocess
import argparse as ap
''' This script opens a bash script, which gets a PDB from PDB Data Bank with another Python Script.
The bash script then opens JMol and takes a picture of the protein

I know this is way overcoded and overthought. You can just use JSMol in Web form for this.

Usage example: --id 1tim --output 1tim

This script may not work on unix machines.'''


parser = ap.ArgumentParser()
parser.add_argument('--id', required=True)
parser.add_argument('--output')
parser.add_argument('--html', action="store_true")
parser.add_argument('--colourized', action="store_true")
args = parser.parse_args()
id2 = str(args.id)
output = str(args.output)
#subprocess.check_output(["visualize_mol.sh", "-i", id2, "-c", "coulour","-o", output], shell=True)
subprocess.check_output(["visualize_mol.sh", "-i", id2,"-o", output], shell=True)

# subprocess.check_output(["bash visualize_mol.sh --i" + id2 +"--o" + output], shell = True)
