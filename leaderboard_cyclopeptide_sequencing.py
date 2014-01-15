import genome

from operator import itemgetter

def expand(leaderboard, weights):
    result = set()
    for weight in weights:
        for candidate in leaderboard:
            newCandidate = candidate + (weight,)
            result.add(newCandidate)
    return result


def sublists(peptide):
    """ Return the circular spectrum of a given peptide."""
    cyclopeptide = peptide + peptide
    for j in xrange(len(peptide)):
        for i in xrange(len(peptide)):
            sublist = cyclopeptide[i:i + j]
            if sublist:
                yield sublist
    yield peptide

def score(peptide, spectrum):
    """ Return score, the number of matching masses between peptide and spectrum."""
    peptide_spectrum = list(sublists(peptide))
    return sum([min(peptide_spectrum.count(p), spectrum.count(p)) for p in peptide_spectrum])

def cut(leaderboard, spectrum, N):
    temp=[]
    for p in leaderboard:
        temp.append((score(p, spectrum), p))
    sorted(temp, key=itemgetter(0))
    result=[]
    for i, x in enumerate(temp):
        if i < N:
            result.append(x[1])
            finalScore = x[0]
        elif finalScore == x[0]:
            result.append(x[1])



if __name__ == "__main__":
    weights = set(genome.readUniqueWeights())

    spectrum = [0, 71, 113, 129, 147, 200, 218, 260, 313, 331, 347, 389, 460]
    N = 10

    inpFile = open('C:/temp/leaderboard_data.txt', 'r')
    inpFile.readline()
    # spectrum = map(int, inpFile.readline().split())

    zero_tuple = 0,
    leaderboard = set()
    leaderboard.add(zero_tuple)
    leaderpeptide = zero_tuple
    while leaderboard:
        leaderboard = expand(leaderboard, weights)
        newLeaderboard = set()
        for peptide in leaderboard:
            if sum(peptide) == max(spectrum):
                if score(peptide, spectrum) > score(leaderpeptide, spectrum):
                    leaderpeptide = peptide
            elif sum(peptide) > max(spectrum):
                None # do nothing, so it isn't in newLeaderboard
            else:
                newLeaderboard.add(peptide)
        leaderboard = cut(newLeaderboard, spectrum, N)


    print '-'.join([str(weight) for weight in leaderpeptide[1:]]),