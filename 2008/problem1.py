import sys
with open("input/problem1.txt") as fs:
	runNum = int(fs.readline())
	for rn in range(runNum):
		thousands_to_rn = {0:"",1:"M",2:"MM",3:"MMM"}
		hundreds_to_rn = {0:"",1:"C",2:"CC",3:"CCC",4:"CD",5:"D",6:"DC",7:"DCC",8:"DCCC",9:"CM"}
		tens_to_rn = {0:"",1:"X",2:"XX",3:"XXX",4:"XL",5:"L",6:"LX",7:"LXX",8:"LXXX",9:"XC"}
		ones_to_rn = {0:"",1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX"}
		ones, tens, hundreds, thousands, = 0,0,0,0
		number = fs.readline().strip()
		length = len(number)
		ones = int(number[-1])
		if  length > 1:
			tens = int(number[-2])
		if length > 2:
			hundreds = int(number[-3])
		if length > 3:
			thousands = int(number[-4])
		print(thousands_to_rn[thousands]+hundreds_to_rn[hundreds]+tens_to_rn[tens]+ones_to_rn[ones])
		
	