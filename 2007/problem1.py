with open("input/problem1.txt") as fs:
    runNum = int(fs.readline())
    for rn in range(runNum):
        m = list()
        inpt = fs.readline()
        r = int(inpt[0])
        c = int(inpt[2])
        ls = int(inpt[4])
        sr = int(inpt[6])
        sc = int(inpt[8])
        x = 0
        count = 0
        while x < r:
            if x == sr:
                x+=1
                l = ""
                for y in range(c):
                    if y ==sc:
                        l +="x"
                    else:
                        l += "o"
                m.append(l)
            elif x >sr and x-sr < ls :
                x+=1
                count +=1
                l = ""
                for y in range(c):
                    if y in range(sc-count,sc+count+1):
                        l+="x"
                    else:
                        l+="o"
                m.append(l)
            elif x >sr and x-sr >= ls:
                x+=1
                l = ""
                count -= 1
                for y in range(c):
                    if y in range(sc-count, sc+count+1):
                        l+="x"
                    else:
                        l+="o"
     
                m.append(l)
            else:
                x+=1
                l = ""
                for j in range(c):
                    l +="o"
                m.append(l)
        for g in range(r):
            print((m[g]))
