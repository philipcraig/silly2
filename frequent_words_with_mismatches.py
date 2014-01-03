import itertools

import genome

def mutations(word, hamming_distance, charset='ATCG'):
    for indices in itertools.combinations(range(len(word)), hamming_distance):
        for replacements in itertools.product(charset, repeat=hamming_distance):
            mutation = list(word)
            for index, replacement in zip(indices, replacements):
                mutation[index] = replacement
            yield "".join(mutation)


def generateMatches(pattern, dict, d):
    dict.update(mutations(pattern, d))


def addMatchesToResults(results, dict):
    for mutation in dict:
        if mutation in results:
            results[mutation] += 1
        else:
            results[mutation] = 1


text = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
k = 10
d = 3

inFile = open('dataset_8_6.txt', 'r')
#inFile.readline()
text = inFile.readline().strip()
# k = int(inFile.readline().strip())
# d = int(inFile.readline().strip())
inFile.close()

i=0
results={}

while i <= len(text) - k:
    section = text[i:i + k]
    dict = set()
    generateMatches(section, dict, d)
    addMatchesToResults(results, dict)
    i += 1

for (k, v) in results.items():
    complement = genome.reversecomplement(k)
    if (complement in results) and (k < complement):
        results[k] += results[complement]
        results[complement] += v

highestFrequency = max(results.values())
for i in [k for k, v in results.items() if v == highestFrequency]:
    print i,

