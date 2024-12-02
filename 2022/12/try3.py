import copy
import string
import sys

sys.setrecursionlimit(100000)
grid = []
STATIC_ALPHABET = string.ascii_lowercase
with open("input.txt") as file:
    lines = file.readlines()
    for line in lines:
        grid.append([])
        for char in line.strip():
            grid[-1].append(char)


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def getHeight(node):
    if node.x < 0 or node.y < 0 or node.x >= len(grid) or node.y >= len(grid[0]):
        raise IndexError
    char = grid[node.x][node.y]
    if char == 'S':
        return STATIC_ALPHABET.index('a')
    elif char == 'E':
        return STATIC_ALPHABET.index('z')
    else:
        return STATIC_ALPHABET.index(char)


def isReachableAndInGrid(node, toNode):
    try:
        heightFrom = getHeight(node)
        heightTo = getHeight(toNode)
        if heightFrom == heightTo  or heightFrom + 1 == heightTo: #or heightFrom - 1 == heightTo
            return True
    except IndexError:
        return False
    return False


def getReachableNeigbors(node):
    reachableNeigbors = []
    if isReachableAndInGrid(node, Node(node.x + 1, node.y)):
        reachableNeigbors.append(Node(node.x + 1, node.y))

    if isReachableAndInGrid(node, Node(node.x - 1, node.y)):
        reachableNeigbors.append(Node(node.x - 1, node.y))

    if isReachableAndInGrid(node, Node(node.x, node.y + 1)):
        reachableNeigbors.append(Node(node.x, node.y + 1))

    if isReachableAndInGrid(node, Node(node.x, node.y - 1)):
        reachableNeigbors.append(Node(node.x, node.y - 1))
    return reachableNeigbors


solutions = []

import threading

threads = []


def recursiveSearch(node, hist, solutions):
    myHist = copy.copy(hist) + (str(node.x) + ',' + str(node.y) + ':')
    if grid[node.x][node.y] == 'E':
        solutions.append(len(myHist) / 4)
        print('Solution found')
    numForThreading=len(getReachableNeigbors(node))
    for nextNode in getReachableNeigbors(node):
        stringToSearch = (str(nextNode.x) + ',' + str(nextNode.y) + ':')
        if myHist.rfind(stringToSearch) == -1:
            if numForThreading > 1:
                thread = threading.Thread(target=recursiveSearch, args=(nextNode, copy.copy(myHist), solutions))
                threads.append(thread)
                thread.start()
            else:
                recursiveSearch(nextNode, copy.copy(myHist), solutions)
        else:
            numForThreading-=1
            # if not (len(hist) > 2 and (str(nextNode.x) + ',' + str(nextNode.y)).__eq__(hist[-2])):
            #    if (str(nextNode.x) + ',' + str(nextNode.y)) not in hist:
            # else:
            #  if not hist.startswith('0,0:1,0'):
        #     print('')
    return


initialNode = Node(20, 0)
recursiveSearch(initialNode, '', solutions)
print(threads)
for thread in threads:
    thread.join()
print(min(solutions) - 1)
