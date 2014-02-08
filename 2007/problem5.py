with open("input/problem5.txt") as fs:
	runNum = int(fs.readline()) // 2
	for rn in range(runNum):
	    line1 = set(fs.readline().split()[1:])
	    line2 = set(fs.readline().split()[1:])
	    difference = line1 ^ line2
	    
	    if not difference:
	        print '-'
	    else:
	        print ' '.join(sorted(difference, key=int))
