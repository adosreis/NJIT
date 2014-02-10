with open("input/problem0.txt") as fs:
	runs = int(fs.readline())
	for _ in range(runs):
		L, W, i = map(int, fs.readline().split())

		m = W - (L - i)
		cost = ((L*W) - (i*m)) * 8

		print L, W, i, cost