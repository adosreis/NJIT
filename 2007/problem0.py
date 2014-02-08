tri = ["000","111","222","333","444","555","666","777","888","999"]
run = ["012","123","234","345","456","567","678","789"]
total = []

total.extend(sorted(x + y) for x in tri for y in tri if x != y)
total.extend(sorted(x + y) for x in tri for y in run)
total.extend(sorted(x + y) for x in run for y in run)

with open("input/problem0.txt") as fs:
    runNum = int(fs.readline())
    for r in range(runNum):
        hand = sorted(fs.readline().split())
        print ("gin" if hand in total else "lose")
