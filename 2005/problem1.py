def divisors(num):
	for x in xrange(1, num):
		if not num % x:
			yield x

with open("input/problem1.txt") as fs:
	runs = int(fs.readline())
	for _ in range(runs):
		num = int(fs.readline())
		total = sum(divisors(num))
		
		print num, "superb" if num < total else "non-superb"