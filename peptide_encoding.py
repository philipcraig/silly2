import genome


def checkCandidate(candidate, results, peptide):
    rna_complement = genome.transpose_rna(genome.reversecomplement(candidate))
    rna = genome.transpose_rna(candidate)
    if genome.encodeProtein(rna) == peptide:
        results.append(candidate)
    elif genome.encodeProtein(rna_complement) == peptide:
        results.append(candidate)


text='ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA'
peptide='VKLFPWFNQY'

inFile = open('B_brevis.txt', 'r')
# inFile.readline()
text=inFile.read().strip()
#peptide=inFile.readline().strip()

codonLength = len(peptide) * 3
i = 0

results=[]

while (i < len(text) - codonLength):
    candidate=text[i:i+codonLength]
    checkCandidate(candidate, results, peptide)
    i += 1

for answer in results:
    print answer
print "Hi"
print len(results)