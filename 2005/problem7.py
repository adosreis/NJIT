def produced(year, version):
	if version == 0:
		return 1
	if version > year:
		return 0

	return produced(year - 1, version) + produced(year - 1, version - 1)

with open("input/problem7.txt") as fs:
	runs = int(fs.readline())
	for _ in range(runs):
		year, version = map(int, fs.readline().split())
		
		print year, version, produced(year, version)