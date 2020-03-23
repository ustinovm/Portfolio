#!/usr/bin/python3
import argparse as ap


'''This script returns the number of incidences of a pattern in a genome'''


parser = ap.ArgumentParser()
# sequences and file input
parser.add_argument("--sequence", type=str, nargs="+", help="Sequence", required=True, action="store", dest="sequences")
parser.add_argument("--genome", type=str, nargs="+", help="The genome", required=True, action="store", dest="genome")

args = parser.parse_args()

seq = args.sequences
genomePath = args.genome

genomePath = str(genomePath[0])

counter = 0

fasta_file = open(genomePath)
fasta = fasta_file.readlines()
fasta_file.close()


class fastaParser:
    '''This class is designed to parse a fasta file and obtain the name and sequence for further analysis.'''
    fasta_dic = {}

    # Until now, a class for opening and parsing only ONE fasta sequence in the file.

    def __init__(self, fasta_input):
        name = ''
        fasta_sequence = ''
        temp = ''
        try:
            for line in fasta_input:
                if line[0] == '>':
                    temp = line.strip('>')
                    temp = temp.rstrip('\n')
                    if name == '':
                        name = temp
                    elif name != temp:
                        self.fasta_dic.update({name: fasta_sequence})
                        name = temp
                        fasta_sequence = ''
                elif line == fasta_input[-1]:
                    fasta_sequence += line.strip('\n')
                    self.fasta_dic.update({name: fasta_sequence})
                else:
                    fasta_sequence += line.strip('\n')
        except:
            print('Fasta sequence not valid.')


def KnuthMorrisPratt(text, pattern):
    #counts the matches of the pattern in the string
    patterny = list(pattern)

    # build table of shift amounts
    shifts = [1] * (len(patterny) + 1)
    shift = 1
    count_matches = 0
    for pos in range(len(patterny)):
        while shift <= pos and patterny[pos] != patterny[pos - shift]:
            shift += shifts[pos - shift]
        shifts[pos + 1] = shift

    # do the actual search
    startPos = 0
    matchLen = 0
    for c in text:
        while matchLen == len(patterny) or \
                matchLen >= 0 and patterny[matchLen] != c:
            startPos += shifts[matchLen]
            matchLen -= shifts[matchLen]
        matchLen += 1
        if matchLen == len(patterny):
            count_matches += 1
            matchLen = 0
    result = count_matches
    return result


fastar = fastaParser(fasta)
dic = fastar.fasta_dic

dicseq = {}
for x in seq:
    dicseq[x] = 0

#iterates over the genome and counts the matches for each pattern
for key in dicseq.keys():
    for y in dic.values():
        dicseq[key] += KnuthMorrisPratt(y, key)

for key, value in dicseq.items():
    print(key+":", value)
