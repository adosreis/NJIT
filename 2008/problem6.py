from itertools import count

with open("input/problem6.txt") as fs:
	polycount = int(fs.readline())

	polys = []

	for power, _ in zip(count(polycount, -1), range(polycount + 1)):

		coeff = int(fs.readline())

		if not coeff:
			continue

		polys += ["+" if coeff > 0 else "-"]
		coeff, power = map(abs, [coeff, power])

		if coeff != 1 or not power:
			polys += [str(coeff)]

		if power > 0:
			s = "x"
			if power != 1:
				s += "^%s" % str(power)
			polys += [s]


	if polys[0] == "+":
		polys.pop(0)

	print " ".join(polys)