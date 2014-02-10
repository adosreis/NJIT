dayNames = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

with open("input/problem2.txt") as fs:
	runs = int(fs.readline())
	for _ in range(runs):
		leapYear, weekday, month, day = map(int, fs.readline().split())
		days = [31, 29 if leapYear else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]

		startDays = [0] * 12
		startDays[0] = weekday - 1

		for i in range(1, 12):
			startDays[i] = (startDays[i-1] + days[i-1]) % 7

		finalWeekday = (startDays[month - 1] + day - 1) % 7

		print leapYear, weekday, month, day, dayNames[finalWeekday]