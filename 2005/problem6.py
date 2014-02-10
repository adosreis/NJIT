import collections

with open("input/problem6.txt") as fs:
	runs = int(fs.readline())
	for _ in range(runs):
		n = int(fs.readline())
		line = collections.deque(range(1, n+1))
		counter = 0
		while len(line) > 1:
			if not counter % 3:
				line.popleft()
			else:
				line.rotate(-1)
			counter += 1

		print n, line[0]
