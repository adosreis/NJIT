from collections import Counter

with open("input/problem3.txt") as fs:
    runNum = int(fs.readline()) // 2
    for _ in range(runNum):
        goal = fs.readline().split()[1:]
        enc = fs.readline().split()[1:]
        
        bag = Counter(enc)
        bag.subtract(goal)

        print "no" if min(bag.values()) < 0 else "yes"
