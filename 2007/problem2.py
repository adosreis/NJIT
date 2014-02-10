import itertools

tests = [map(int, x) for x in ["111000000", "000111000", "000000111", "100100100", "010010010", "001001001", "100010001", "001010100"]]

def test(pattern, val):
    for test in tests:
        if all(x == val for x in itertools.compress(pattern, test)):
            return True
    return False

with open("input/problem2.txt") as fs:
    runNum = int(fs.readline())
    for _ in range(runNum):
        row = list(itertools.chain.from_iterable([fs.readline().split() for x in range(3)]))
        if test(row, "X"):
            print "X"
        elif test(row, "O"):
            print "O"
        else:
            print "-"