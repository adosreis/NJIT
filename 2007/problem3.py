with open("input/problem3.txt") as fs:
    runNum = int(fs.readline()) // 2
    for rn in range(runNum):
        goal = fs.readline().split()[1:]
        enc = fs.readline().split()[1:]
        for c in goal:
            if not c in enc:
                print "no"
                break
            else:
                enc.remove(c)
        else:
            print "yes"
