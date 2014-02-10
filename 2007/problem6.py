with open("input/problem6.txt") as fs:
	runNum = int(fs.readline())
	for _ in range(runNum):
		nB, n1, tD, = map(int, fs.readline().split())
		for y in range(tD):
			nB, n1 = n1*2, nB
		print nB + n1