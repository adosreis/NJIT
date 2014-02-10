with open("input/problem4.txt") as fs:
    runNum = int(fs.readline())
    for _ in range(runNum):
        group = fs.readline().split()[1:]
        gl = len(group)
        group.sort()

        sort = []
        mid = gl // 2

        for i in range(mid):
            sort.append(group[i])
            sort.append(group[i + mid])

        if gl % 2:
            sort.insert(-1, group[-1])

        print ' '.join(sort)
