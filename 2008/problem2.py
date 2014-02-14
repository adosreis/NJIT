from itertools import groupby

with open("input/problem2.txt") as fs:
	runs = int(fs.readline())
	for _ in range(runs):
		print " ".join("%s:%s" % (len(list(g)), v) for v,g in groupby(fs.readline().strip()))