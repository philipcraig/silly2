import genome


def expandCandidates(candidates, weights):
    result = []
    for weight in weights:
        for candidate in candidates:
            newCandidate=[]
            newCandidate.extend(candidate)
            newCandidate.extend([weight])
            result.append(newCandidate)
    return result

weights = set(genome.readUniqueWeights())

spectrum = [0,113,128,186,241,299,314,427]

candidates = [[0]]
while len(candidates) > 0:
    candidates = expandCandidates(candidates, weights)
    # for peptide in list:
    i = 0
    while i < len(candidates):
        peptide = candidates[i]
        if sum(peptide) == spectrum[-1]:
            print peptide[1:]
            candidates.remove(peptide)
        elif sum(peptide) not in spectrum:
            candidates.remove(peptide)
        else:
            i += 1