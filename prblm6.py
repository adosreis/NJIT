import sys
fs = open("prblm6.txt")
runNum = int(fs.readline())
for rn in range(runNum):
	nB, n1, tD, = map(int, fs.readline().split())
	for y in range(tD):
		nB, n1 = n1*2,nB
		population = nB + n1
	print(population)