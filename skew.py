inFile = open('C:\\temp\\dataset_7_6.txt', 'r')
# pattern='CTTGATCAT' # inFile.readline().strip()
genome = inFile.readline().strip()

results = []
currentSkew = 0
bestSkew = 1 # so that it will get overriden on first pass below

i=0
while i < len(genome):
    if currentSkew == bestSkew:
        results.append(i) # add new location but leaving old ones as equal
    elif currentSkew < bestSkew:
        results = [] # throw away former results as we have a new best
        results.append(i)
        bestSkew = currentSkew
    c = genome[i]
    if c == 'C':
        currentSkew -=1
    elif c == 'G':
        currentSkew += 1
    i += 1

for i in results:
    print i,