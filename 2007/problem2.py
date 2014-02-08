import itertools

working = [0b111000000, 0b000111000, 0b000000111, 0b100100100, 0b010010010, 0b001001001, 0b100010001, 0b001010100]

def test(pattern, val):
    changed = int("".join([("1" if x == val else "0") for x in pattern]), 2)
    for work in working:
        if changed & work == work:
            return True
    return False

with open("input/problem2.txt") as fs:
    runNum = int(fs.readline())
    for rn in range(runNum):
        row = list(itertools.chain.from_iterable([fs.readline().split() for x in range(3)]))
        if test(row, "X"):
            print "X"
            continue
        if test(row, "O"):
            print "O"
            continue
        print "-"