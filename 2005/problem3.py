with open("input/problem3.txt") as fs:
	runs = int(fs.readline()) // 3
	for _ in range(runs):
		startingSet = set(map(int, fs.readline().split()))
		startingSet.intersection_update(map(int, fs.readline().split()))
		startingSet.intersection_update(map(int, fs.readline().split()))

		print ' '.join(map(str, sorted(startingSet)))