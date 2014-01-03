import itertools

import genome

peptide = "LEQN"

peptide = open('dataset_20_3.txt', 'r').readline().strip()

result=[]

weights = genome.readWeights()

for a in genome.subpeptides(peptide):
    sum=0
    for i in a:
        sum += weights[i]
    result.append(sum)


for i in sorted(result):
    print i,