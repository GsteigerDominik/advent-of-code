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


def move(fromX, fromY, toX, toY):
    print(fromX,fromY,toX,toY)
    if grid[fromX][fromY]== 'S':
        fromHeight=0
    else:
        fromHeight = STATIC_ALPHABET.index(grid[fromX][fromY])
    try:
        if grid[toX][toY]== 'E' and fromHeight >= STATIC_ALPHABET.index('y'):
            print('Found it ')
        else:
            if grid[toX][toY]== 'S':
                toHeight=0
            else:
                toHeight = STATIC_ALPHABET.index(grid[toX][toY])
            if fromHeight==toHeight or fromHeight + 1 == toHeight:
                move(toX,toY,toX+1,toY)
                move(toX,toY,toX-1,toY)
                move(toX,toY,toX,toY+1)
                move(toX,toY,toX,toY-1)
            else:
                return
    except IndexError:
        return
move(0,0,0,0)