import genome


def expandCandidates(candidates, weights):
    result = set()
    for weight in weights:
        for candidate in candidates:
            newCandidate = candidate + (weight,)
            result.add(newCandidate)
    return result


def sublists(peptide):
    for j in range(len(peptide)):
        for i in range(len(peptide) - j + 1):
            yield peptide[i:i + j]

def consistent(peptide, spectrum):
    for candidate in sublists(peptide):
        if sum(candidate) not in spectrum:
            return False
    return True

weights = set(genome.readUniqueWeights())

spectrum = [0, 113, 128, 186, 241, 299, 314, 427]

inpFile = open('C:/temp/dataset_22_4.txt', 'r')
# inpFile.readline()
spectrum = map(int, inpFile.readline().split())

zero_tuple=0,
candidates = set()
candidates.add(zero_tuple)
while candidates:
    candidates = expandCandidates(candidates, weights)
    newCandidates = set()
    for peptide in candidates:
        if sum(peptide) == spectrum[-1]:
            print '-'.join([str(weight) for weight in peptide[1:]]),

        elif not consistent(peptide, spectrum):
            None # do nothing, so it isn't in newCandidates
        else:
            newCandidates.add(peptide)
    candidates = newCandidates