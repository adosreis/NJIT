import sys
fs = open("prblm5.txt")
runNum = int(fs.readline())//2
for rn in range(runNum):
    line1 =fs.readline().split()[1:]
    line2 =fs.readline().split()[1:]
    difference = list(set(line1)^set(line2))
    if not difference:
        print('-')
    else:
        print(' '.join(sorted(difference, key=int)))
