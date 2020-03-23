#!/usr/bin/python3

import urllib.request
import argparse
import os.path
import shutil
import tempfile
'''This script downloads a PDB from the PDB Databank'''


parser = argparse.ArgumentParser()
parser.add_argument("--id", type=str, help="PDB ID", required=True, action="store",
                    dest="pdb_id")
parser.add_argument("--output", dest="output", help="Output file", action="store")
parser.add_argument("--fasta", help="output a .fasta", action="store_true")

args = parser.parse_args()
output = args.output
pdb_id = args.pdb_id


def download_fasta_andstrorstdout(pdb_idf, store):
    fasta_clean = ""
    if store:
        urllib.request.urlretrieve(
            "https://www.rcsb.org/pdb/download/downloadFastaFiles.do?structureIdList=" + pdb_idf +
            "&compressionType=uncompressed", output + pdb_idf + ".fasta")
    else:
        with urllib.request.urlopen(
                "https://www.rcsb.org/pdb/download/downloadFastaFiles.do?structureIdList=" + pdb_idf +
                "&compressionType=uncompressed") as response:
            with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
                shutil.copyfileobj(response, tmp_file)


        with open(tmp_file.name) as html:
            for line in html:
                fasta_clean += line
        print(fasta_clean)


def download_pdb_andstrorstdout(pdb_idf, store):
    pdb_clean = ""
    if store:
        urllib.request.urlretrieve('https://files.rcsb.org/download/' + pdb_idf + ".pdb", output)
    else:
        with urllib.request.urlopen('https://files.rcsb.org/download/' + pdb_idf + ".pdb") as response:
            with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
                shutil.copyfileobj(response, tmp_file)

        with open(tmp_file.name) as html:
            for line in html:
                pdb_clean += line
        print(pdb_clean)
    pass


if output == "-":
    if args.fasta:
        download_fasta_andstrorstdout(pdb_id, False)
    else:
        download_pdb_andstrorstdout(pdb_id, False)
elif args.fasta:
    download_fasta_andstrorstdout(pdb_id, True)
else:
    download_pdb_andstrorstdout(pdb_id, True)
