from collections import Counter

with open("input/problem4.txt") as fs:
	runs = int(fs.readline())

	for _ in range(runs):
		word1, word2 = fs.readline().strip().split()
		lcounter = Counter(word1)
		lcounter.subtract(word2)

		print "true" if min(lcounter.values()) >= -1 else "false"