units = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def encode(n):
	if n < 20:
		return units[n]
	elif n < 100:
		return " ".join(filter(None, [tens[n // 10], units[n % 10]]))
	elif n < 1000:
		return " ".join(filter(None, [units[n // 100], "hundred", encode(n % 100)]))
	else:
		return " ".join(filter(None, [encode(n // 1000), "thousand", encode(n % 1000)]))

with open("input/problem0.txt") as fs:
	runs = int(fs.readline())
	for _ in range(runs):
		n = int(fs.readline())

		print encode(n)