with open("input/problem7.txt") as fs:
	runNum = int(fs.readline())
	for rn in range(runNum):
		tickets = map(int, fs.readline().split())
		miles = tickets.pop(0)

		for x in xrange(2 ** 10):
			total = sum(v if x & (1 << i) == 1 << i else -v for i, v in enumerate(tickets))
			if total == miles:
				print "turkey"
				break
		else:
			print "pizza"
