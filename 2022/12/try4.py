import copy
import string
import threading
import sys

grid = []
STATIC_ALPHABET = string.ascii_lowercase
sys.setrecursionlimit(100000)

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def notInGrid(x, y):
    try:
        grid[x][y]
    except IndexError:
        return True
    return False


def notInGridAndNotReachable(height, x, y):
    return notInGrid(x, y) or abs(height - grid[x][y]) > 1


def notReachable(x, y):
    myHeigt = grid[x][y]
    if notInGridAndNotReachable(myHeigt, x + 1, y) and \
            notInGridAndNotReachable(myHeigt, x - 1, y) and \
            notInGridAndNotReachable(myHeigt, x, y + 1) and \
            notInGridAndNotReachable(myHeigt, x, y - 1):
        return True
    return False


def oneWayIn(x, y):
    myHeigt = grid[x][y]
    counter = 0
    if notInGridAndNotReachable(myHeigt, x + 1, y):
        counter += 1
    if notInGridAndNotReachable(myHeigt, x - 1, y):
        counter += 1
    if notInGridAndNotReachable(myHeigt, x, y + 1):
        counter += 1
    if notInGridAndNotReachable(myHeigt, x, y - 1):
        counter += 1
    if counter == 3:
        print(x, y)
        return True
    return False


with open("input.txt") as file:
    lines = file.readlines()
    for line in lines:
        grid.append([])
        for char in line.strip():
            grid[-1].append(char)

lineIdx = 0
for line in grid:
    charIdx = 0
    for char in line:
        if char == 'S':
            grid[lineIdx][charIdx] = -1
        elif char == 'E':
            grid[lineIdx][charIdx] = 26
        else:
            grid[lineIdx][charIdx] = STATIC_ALPHABET.index(char)
        charIdx += 1
    lineIdx += 1

lineIdx = 0
# for line in grid:
#    charIdx = 0
#    for char in line:
#        if notReachable(lineIdx, charIdx):
#            grid[lineIdx][charIdx] = -3
#        if oneWayIn(lineIdx, charIdx):
#            print('')
#            # grid[lineIdx][charIdx]=-4
#        charIdx += 1
#    lineIdx += 1

for line in grid:
    string = ''
    for char in line:
        if char == -1:
            string = string + 'SS '
        #elif char == -3:  # or char==-4:
        #    string = string + 'XX '
        elif char <= 9:
            string = string + '0' + str(char) + ' '
        else:
            string = string + str(char) + ' '
    print(string)


def isReachableAndInGrid(node, toNode):
    try:
        heightFrom = 0
        if grid[node.x][node.y] == 'SS':
            heightFrom = 1
        else:
            heightFrom = int(grid[node.x][node.y])
        heightTo = int(grid[toNode.x][toNode.y])

        if heightFrom == heightTo or heightFrom + 1 == heightTo:  # or heightFrom - 1 == heightTo
            return True
    except IndexError:
        return False
    return False


def getReachableNeigbors(node):
    reachableNeigbors = []
    if node.x < len(grid)/2:
        if isReachableAndInGrid(node, Node(node.x + 1, node.y)):
            reachableNeigbors.append(Node(node.x + 1, node.y))
        if isReachableAndInGrid(node, Node(node.x - 1, node.y)):
           reachableNeigbors.append(Node(node.x - 1, node.y))
    else:
        if isReachableAndInGrid(node, Node(node.x - 1, node.y)):
            reachableNeigbors.append(Node(node.x - 1, node.y))
        if isReachableAndInGrid(node, Node(node.x + 1, node.y)):
            reachableNeigbors.append(Node(node.x + 1, node.y))
    if node.y < len(grid[0])/2:
        if isReachableAndInGrid(node, Node(node.x, node.y + 1)):
            reachableNeigbors.append(Node(node.x, node.y + 1))
        if isReachableAndInGrid(node, Node(node.x, node.y - 1)):
            reachableNeigbors.append(Node(node.x, node.y - 1))
    else:
        if isReachableAndInGrid(node, Node(node.x, node.y - 1)):
            reachableNeigbors.append(Node(node.x, node.y - 1))
        if isReachableAndInGrid(node, Node(node.x, node.y + 1)):
            reachableNeigbors.append(Node(node.x, node.y + 1))
    return reachableNeigbors


threads = []


def recursiveSearch(node, depth, lastNode, solutions):
    myDepth = depth + 1
    print(STATIC_ALPHABET.__getitem__(grid[node.x][node.y])+str(node.x)+','+str(node.y))
    if grid[node.x][node.y] == 26:
        solutions.append(myDepth)
        print('Solution found')

    for nextNode in getReachableNeigbors(node):
        if not (nextNode.x == lastNode.x and nextNode.y == lastNode.y):
            if len(threads) < 800:
                thread = threading.Thread(target=recursiveSearch, args=(nextNode, myDepth, node, solutions))
                threads.append(thread)
                thread.start()
            else:
                recursiveSearch(nextNode, myDepth, node, solutions)
            # if not (len(hist) > 2 and (str(nextNode.x) + ',' + str(nextNode.y)).__eq__(hist[-2])):
            #    if (str(nextNode.x) + ',' + str(nextNode.y)) not in hist:
            # else:
            #  if not hist.startswith('0,0:1,0'):
        #     print('')
    return


solutions = []
initialNode = Node(20, 0)
recursiveSearch(initialNode, 0,initialNode, solutions)
print(threads)
for thread in threads:
    thread.join()
#print(min(solutions) - 1)
