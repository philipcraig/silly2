from toolset import *


def addToDict(dict, group, results, t):
    if group in dict:
        dict[group] += 1
    else:
        dict[group] = 1
    if dict[group] >= t:
        results[group] = True


inFile = open('E-coli.txt', 'r')
# pattern='CTTGATCAT' # inFile.readline().strip()
testGenome = inFile.readline().strip()
numbers = inFile.readline().split()
k = int(numbers[0])
L = int(numbers[1])
t = int(numbers[2])
results = {}
i = 1
dict = {}
for foo in groups(testGenome[0:L], k, 1):
    addToDict(dict, ''.join(foo), results, t)

while i < len(testGenome) - L:
    groupToRemove = testGenome[i - 1:i + k - 1]
    dict[groupToRemove] -= 1 # remove last entry from slide
    groupToAdd = testGenome[i + L - k:i + L]
    addToDict(dict, groupToAdd, results, t)
    i += 1

for candidate in results.keys():
    print candidate,
print "hi"
print len(results)

# positions = [m.start() for m in re.finditer('(?='+pattern+')', testGenome)]
# for pos in positions:
#     print pos,

inFile.close()