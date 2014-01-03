import genome

weights = genome.readUniqueWeights()

spectrum = [0,113,128,186,241,299,314,427]

list = [[0]]
#while len(result) != 0:

expandList(list)
for peptide in list:
    if