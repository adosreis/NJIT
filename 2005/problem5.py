from collections import Counter

def sort_str(s):
	return ''.join(sorted(s))

with open("input/problem5.txt") as fs:
	runs = int(fs.readline())
	counts = Counter()

	inputs = [fs.readline().strip() for _ in range(runs)]

	counts.update(map(sort_str, inputs))
	
	for num in inputs:
		if counts[sort_str(num)] == 1:
			print num
