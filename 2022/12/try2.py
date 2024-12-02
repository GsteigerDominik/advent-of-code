import string
import sys

sys.setrecursionlimit(100000)
STATIC_ALPHABET = string.ascii_lowercase

grid = []
with open("input.txt") as file:
    lines = file.readlines()
    for line in lines:
        grid.append([])
        for char in line.strip():
            grid[-1].append(char)
print(grid)


def getHeight(x, y):
    char = grid[x][y]
    if char == 'S':
        return STATIC_ALPHABET.index('a')
    elif char == 'E':
        return STATIC_ALPHABET.index('z')
    else:
        return STATIC_ALPHABET.index(char)


def isReachable(x, y, toX, toY):
    try:
        heightFrom = getHeight(x, y)
        heightTo = getHeight(toX, toY)
        if heightFrom == heightTo or heightFrom - 1 == heightTo or heightFrom + 1 == heightTo:
            return True
    except IndexError:
        print('Index happend')
        return False
    return False


def getKeyFromXY(x, y):
    return str(x) + ',' + str(y)


def recursivePathFinding(nodeX, nodeY, positionVisited):
    positionVisited[getKeyFromXY(nodeX, nodeY)] = 0
    if grid[nodeX][nodeY] == 'Z':
        print('Ziel erreicht')
        return print(positionVisited)
    if isReachable(nodeX, nodeY, nodeX + 1, nodeY) and getKeyFromXY(nodeX + 1, nodeY) not in positionVisited:
        recursivePathFinding(nodeX + 1, nodeY, positionVisited)
    if isReachable(nodeX, nodeY, nodeX - 1, nodeY) and getKeyFromXY(nodeX - 1, nodeY) not in positionVisited:
        recursivePathFinding(nodeX - 1, nodeY, positionVisited)
    if isReachable(nodeX, nodeY, nodeX, nodeY + 1) and getKeyFromXY(nodeX, nodeY + 1) not in positionVisited:
        recursivePathFinding(nodeX, nodeY + 1, positionVisited)
    if isReachable(nodeX, nodeY, nodeX, nodeY - 1) and getKeyFromXY(nodeX, nodeY - 1) not in positionVisited:
        recursivePathFinding(nodeX, nodeY - 1, positionVisited)
    return print(positionVisited)


startX = 0
startY = 0
recursivePathFinding(startX, startY, {})
