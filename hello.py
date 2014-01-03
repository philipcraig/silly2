import re

import genome

inFile=open('dataset_18_3.txt', 'r')
pattern='AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
pattern=inFile.readline().strip()
print genome.encodeProtein(pattern)