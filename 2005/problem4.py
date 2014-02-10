import collections

rankings = '234567890JQKA'

def process(hand):
	counts = collections.Counter(map(rankings.find, hand))
	def lookup(x):
		return [v for v, k in counts.items() if k == x]

	def lookup_one(x):
		return lookup(x)[0]

	#four of a kind
	if lookup(4):
		return (6,) + (lookup_one(4),) * 4 + (lookup_one(1),)
	#full house
	if lookup(3) and lookup(2):
		return (5,) + (lookup_one(3),) * 3 + (lookup_one(2),) * 2
	#straight
	if len(counts) == 5 and (max(counts) - min(counts) == 4):
		return (4,) + tuple(sorted(counts, reverse=True))
	#three of a kind
	if lookup(3):
		return (3,) + (lookup_one(3),) * 3 + tuple(sorted(lookup(1), reverse=True))
	#two pairs
	if len(lookup(2)) == 2:
		return (2,) + tuple(sorted(lookup(2) * 2, reverse=True)) + (lookup_one(1),)
	#one pair
	if len(lookup(2)) == 1:
		return (1,) + (lookup_one(2),) * 2 + tuple(sorted(lookup(1), reverse=True))

	return (0,) * 6

with open("input/problem4.txt") as fs:
	runs = int(fs.readline())
	for _ in range(runs):
		first, second = fs.readline().split()
		print first, second,
		firstProcessed, secondProcessed = process(first), process(second)
		if firstProcessed < secondProcessed:
			print 2
		elif firstProcessed > secondProcessed:
			print 1
		else:
			print 0

