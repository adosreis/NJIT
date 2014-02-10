import textwrap

def fmt(s):
	wrapped = textwrap.wrap(s, 79)
	if len(wrapped[-1]) == 1 and len(wrapped) > 1:
		wrapped[-2] += wrapped[-1]
		del wrapped[-1]
	return '&\n'.join(wrapped)

with open("input/problem8.txt") as fs:
	runs = int(fs.readline()) // 2
	for _ in range(runs):
		first = int(fs.readline())
		second = int(fs.readline())
		
		print first
		print second
		print fmt(str(first + second))
		print first - second
		print fmt(str(first * second))
		print first // second