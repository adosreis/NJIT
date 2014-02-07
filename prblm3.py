import sys
fs = open("prblm3.txt")
runNum = int(fs.readline()) // 2
for rn in range(runNum):
    _, *goal = fs.readline().split()
    _, *enc = fs.readline().split()
    for c in goal:
        if not c in enc:
            print("False")
            break
        else:
            enc.remove(c)
    else:
        print("True")
