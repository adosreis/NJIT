with open("input/problem5.txt") as fs:
	runs = int(fs.readline())
	votes = []
	for _ in range(runs):
		votes.append(map(int, fs.readline().strip().split()))

	people = set(range(1, runs + 1))

	for vote in votes:
		people.intersection_update(set(i for i, v in enumerate(vote, 1) if v))

	people = list(people)
	if not people or votes[people[0] - 1].count(1) > 1:
		print "none"
	else:
		print people[0]