import itertools


def matches(section, dict):
    if section in dict:
        return True
    else:
        return False


def mutations(word, hamming_distance, charset='ATCG'):
    for indices in itertools.combinations(range(len(word)), hamming_distance):
        for replacements in itertools.product(charset, repeat=hamming_distance):
            mutation = list(word)
            for index, replacement in zip(indices, replacements):
                mutation[index] = replacement
            yield "".join(mutation)


def generateMatches(pattern, dict, d):
    dict.update(mutations(pattern, d))


text = 'CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT'
pattern = 'ATTCTGGA'
d = 3

inFile = open('dataset_8_3.txt', 'r')
# pattern='CTTGATCAT' # inFile.readline().strip()
pattern = inFile.readline().strip()
text = inFile.readline().strip()
d = int(inFile.readline().strip())

i=0
dict=set()
generateMatches(pattern, dict, d)
results=[]

while i <= len(text) - len(pattern):
    section = text[i:i + len(pattern)]
    if matches(section, dict):
        results.append(i)
    i += 1

for i in results:
    print i,