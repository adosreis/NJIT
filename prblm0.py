runNum = int(input())
for r in range(runNum):
    totalPos=([])
    pos1=(["000"])
    pos2=([])
    for x in range(10):
        pos1.append(str(x*111))
    for i in range(8):
        pos2.append("0123456789"[i:i+3])
    for y in range(10):
        for j in range(8):
            add1 = list(pos1[y]+pos2[j])
            add1.sort()
            add2 = list(pos1[y+1]+pos1[j])
            add2.sort()
            totalPos.append(str(add1))
            totalPos.append(str(add2))
            if(y > 0) and (y<len(pos2)):
                add3 =list(pos2[y-1]+pos2[j])
                add3.sort()
                totalPos.append(str(add3))
    totalPos=set(totalPos)
    hand = list(input())
    hand.sort()
    hand = str(hand)
    if hand in totalPos:
        print("gin")
    else:
        print("lose")
