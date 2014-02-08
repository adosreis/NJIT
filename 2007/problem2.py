with open("input/problem2.txt") as fs:
    runNum = int(fs.readline())
    for rn in range(runNum):
        row = [fs.readline().split() for x in range(3)]
        print(row)
        worked = False
        for x in range(0,3):
            if row[x][0] == row[x][1] == row[x][2]:
                print(row[x][0])
                worked = True
        if row[0][0] == row[1][1] == row[2][2]:
            print(row[0][0])
            worked = True
        elif row[0][2] == row[1][1] == row[2][0]:
            print(row[2][0])
            worked = True
        for x in range(0,3):
            if row[0][x] == row[1][x] == row[2][x]:
                print(row[0][x])
                worked = True
        if not worked :
            print('-')
    
