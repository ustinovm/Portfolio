#!/usr/bin/python3
import argparse as ap
import urllib.request
import re
from urllib.error import HTTPError

''' script takes a search term and returns the number of results for that organism in Swissprot and TrEMBL.
Swissprot contains reviewed entries, TrEMBL unreviewed ones. 
Note that the results are specified for the column "organism", not the general search'''

parser = ap.ArgumentParser()
parser.add_argument('--org', required=True)
args = parser.parse_args()

organism = args.org
organism = re.sub(r'\W+', '+', organism)

# finds results in TrEMBL/unreviewed results

url = ('https://www.uniprot.org/uniprot/?query=organism%3A' + organism)
trembl = '&fil=reviewed%3Ano&format=list&compress=no'
swiss = '&fil=reviewed%3Ayes&format=list&compress=no'
try:
    with urllib.request.urlopen(url+trembl) as data:
        data = data.read().decode('utf-8')
        listing = data.split('\n')
        print("TrEMBL " + str(len(listing) - 1))
    with urllib.request.urlopen(url+swiss) as data2:
        data2 = data2.read().decode('utf-8')
        listing2 = data2.split('\n')
        print("Swissprot " + str(len(listing2) - 1))
except HTTPError as err:
    if err.code == 404:
        print("!URL is not valid!")
    if err.code == 400:
        print("Bad input!")

# finds results in Swissprot/reviewed results
