# a can be assumed to be rectangular.


def BetterZeroField(x, y):
    return [[0] * x for i in range(y)]


def rotate(a):
    nRows = len(a[0])
    nCol = len(a)
    b = BetterZeroField(nCol, nRows)
    for y in range(nCol - 1, -1, -1):
        for x in range(nRows):
            print(nCol - 1 - y)
            b[x][y] = a[nCol-1 - y][x]
    return b

def rotate2(a):
    nRows = len(a[0])
    nCol = len(a)
    b = []
    for x in range(nRows):
        b.append([])
        for y in range(nCol - 1, -1, -1):
            b[x].append(a[y][x])
    return b

print(rotate2([[1, 1, 1], [0, 1, 0], [0, 1, 0]]))