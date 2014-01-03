from __future__ import division

import csv

def complement(symbol):
    if symbol == 'A':
        return 'T'
    elif symbol == 'T':
        return 'A'
    elif symbol == 'G':
        return 'C'
    elif symbol == 'C':
        return 'G'
    else:
        return ''

def reversecomplement(inp):
    result=''
    for symbol in reversed(inp):
        result += str(complement(symbol))
    return result


def transpose_rna(inp):
    return inp.replace("T", "U")


def isgc(symbol):
    return symbol == 'G' or symbol == 'C'


def gclength(dna):
    gc=0
    for symbol in dna:
        if isgc(symbol):
            gc += 1
    return gc

def gcPercent(dna):
    return gclength(dna) / len(dna) * 100.0


def fasta_parse(fastaFile):
    inpFile=open(fastaFile, 'r')

    strings = {}
    lastLabel='x'
    gcContent = 0.0
    dna='x'

    for line in inpFile.readlines():
        if line[0] == '>':
            label = line[1:]
            strings[gcPercent(dna)] = lastLabel
            lastLabel = label
            dna=''
        else:
            dna += line.rstrip('\n')

    strings[gcPercent(dna)]=lastLabel
    return strings

def hamming(s, t):
    result = 0
    i=0
    if len(s) != len(t):
        exit(-1)
    else:
        for symbol in s:
            if symbol != t[i]:
                result += 1
            i += 1
    return result

def kmer(string, k):
    result = {}
    if (k < 1) or (k > len(string)):
        exit(-1)
    else:
        i=0
        while i <= len(string) - k:
            candidate = string[i:i+k]
            if result.has_key(candidate):
                result[candidate] += 1
            else:
                result[candidate] = 1
            i += 1
    return result

def readCodons():
    inpFile = open('rna_codons.txt')
    result = {}
    for line in inpFile.readlines():
        result[line[0:3]] = line[4:].strip()
    inpFile.close()
    return result


def readWeights():
    with open('integer_mass_table.txt', 'r') as f:
        weights = {}
        for ln in f:
            (letter, weight) = ln.split()
            weights[letter] = int(weight)
    return weights


def readUniqueWeights():
    weights = readWeights()
    return weights.values()

def subpeptides(peptide):
    l = len(peptide)
    looped = peptide + peptide
    yield ''
    for start in range(0, l):
        for length in range(1, l):
            yield looped[start:start+length]
    yield peptide


def encodeProtein(rnaString):
    codons=readCodons()
    i=0
    result = ''
    if len(rnaString) % 3 != 0:
        exit(-1)
    while i < len(rnaString):
        protein=codons[rnaString[i:i+3]]
        if protein != 'Stop':
            result += protein
            i+=3
        else:
            return result
    return result
