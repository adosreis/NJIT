thou_to_rn = {"0": "", "1": "M", "2": "MM", "3": "MMM"}
hund_to_rn = {"0": "", "1": "C", "2": "CC", "3": "CCC", "4": "CD", "5": "D", "6": "DC", "7": "DCC", "8": "DCCC", "9": "CM"}
tens_to_rn = {"0": "", "1": "X", "2": "XX", "3": "XXX", "4": "XL", "5": "L", "6": "LX", "7": "LXX", "8": "LXXX", "9": "XC"}
ones_to_rn = {"0": "", "1": "I", "2": "II", "3": "III", "4": "IV", "5": "V", "6": "VI", "7": "VII", "8": "VIII", "9": "IX"}

with open("input/problem1.txt") as fs:
	runNum = int(fs.readline())
	for _ in range(runNum):
		number = fs.readline().strip()

		result = ""

		length = len(number)

		if length > 3:
			result += thou_to_rn[number[-4]]
		if length > 2:
			result += hund_to_rn[number[-3]]
		if  length > 1:
			result += tens_to_rn[number[-2]]

		result += ones_to_rn[number[-1]]


		print result
		
	