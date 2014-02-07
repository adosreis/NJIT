import sys
from random import shuffle
fs = open("prblm7.txt")
runNum = int(fs.readline())
for rn in range(runNum):
	info = fs.readline().split()
	dHome = info.pop(0)
	alreadyDone = []
	while(True):
		shuffle(info)
		if list(info) not in set(alreadyDone):
       		alreadyDone.add(list(info))
       		north = info[:5]
			south = info[5:]
			northSum = int(0)
			southSum = int(0)
			for x in range(5):
				northSum += int(north[x])
				southSum -= int(south[x])
			totalMove = northSum-southSum
			if (int(totalMove) - int(dHome) == 0):
				print(Turkey)
				break




	
