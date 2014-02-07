import sys
fs = open("prblm4.txt")
runNum = int(fs.readline())
for rn in range(runNum):
    gl, *group = fs.readline().split()
    gl = int(gl)
    group.sort()
    asc = group[0:gl//2+1]
    des = group[gl//2+1:gl]
    asc.sort()
    des.sort()
    count = 0
    for i in range(1,gl//3+1):
        tempList = list(asc[i:])
        tempList.reverse()
        asc[i:] = tempList
    for x in range(gl//3+1):
        tempList = list(des[x:])
        tempList.reverse()
        des[x:] = tempList
    sort = asc + des
    print(sort)
