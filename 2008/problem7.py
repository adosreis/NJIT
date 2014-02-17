from sys import exit
from functools import partial

with open("input/problem7.txt") as fs:
	line = ''.join([''.join(fs.readline().split()) for _ in range(4)])

	same_row = lambda i, j: i // 4 == j // 4
	same_column = lambda i, j: (i - j) % 4 == 0
	same_block = lambda i, j: i // 8 == j // 8 and i % 4 // 2 == j % 4 // 2

	def r(s):
		i = s.find("0")
		if i == -1:
			print "\n".join(map(partial(str.join, " "), zip(*([iter(s)] * 4))))
			exit()

		excluded = {s[j] for j in range(16) if same_row(i, j) or same_column(i, j) or same_block(i, j)}

		for m in "1234":
			if m not in excluded:
				r(s[:i] + m + s[i+1:])

	r(line)