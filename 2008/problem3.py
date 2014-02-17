replaces = [
	("ies", "y", ("eies", "aies")),
	("es", "e", ("aes", "ees", "oes")),
	("s", "", ("us", "ss"))
]

def replace(s):
	for m in replaces:
		if s.endswith(m[0]) and not s.endswith(m[2]):
			return s.rpartition(m[0])[0] + m[1]
	
	return s

with open("input/problem3.txt") as fs:
	runs = int(fs.readline())
	for _ in range(runs):
		print replace(fs.readline().strip())