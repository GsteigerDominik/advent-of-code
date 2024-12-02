import math


class Position:

    def __init__(self, x, y, nextNode):
        self.x = x
        self.y = y
        self.nextNode = nextNode
        self.tailWasHere = {}

    def print(self):
        if self.nextNode is None:
            print('Tail')
        else:
            print('Head or Middle')
        print('X:' + str(self.x) + ' Y:' + str(self.y))


def moveRight(position, num):
    for num in range(num):
        position.x += 1
        moveTail(position, position.nextNode)


def moveLeft(position, num):
    for num in range(num):
        position.x -= 1
        moveTail(position, position.nextNode)


def moveUp(position, num):
    for num in range(num):
        position.y += 1
        moveTail(position, position.nextNode)


def moveDown(position, num):
    for num in range(num):
        position.y -= 1
        moveTail(position, position.nextNode)


def isNotDiagonal(head, tail):
    return 2 < math.sqrt(abs(head.x - tail.x) ** 2) + math.sqrt(abs(head.y - tail.y) ** 2)


def moveTail(head, tail):
    if head.y == tail.y or head.x == tail.x:
        if head.x > tail.x + 1:
            tail.x += 1
        elif head.x < tail.x - 1:
            tail.x -= 1
        elif head.y > tail.y + 1:
            tail.y += 1
        elif head.y < tail.y - 1:
            tail.y -= 1
    else:
        if isNotDiagonal(head, tail):
            if head.x > tail.x:
                tail.x += 1
            else:
                tail.x -= 1
            if head.y > tail.y:
                tail.y += 1
            else:
                tail.y -= 1
    string = str(tail.x) + ',' + str(tail.y)
    tail.tailWasHere[string] = 0
    if tail.nextNode is not None:
        moveTail(tail, tail.nextNode)


COMMANDS = {
    'R': moveRight,
    'L': moveLeft,
    'U': moveUp,
    'D': moveDown
}

tail9 = Position(0, 0, None)
tail8 = Position(0, 0, tail9)
tail7 = Position(0, 0, tail8)
tail6 = Position(0, 0, tail7)
tail5 = Position(0, 0, tail6)
tail4 = Position(0, 0, tail5)
tail3 = Position(0, 0, tail4)
tail2 = Position(0, 0, tail3)
tail1 = Position(0, 0, tail2)
head = Position(0, 0, tail1)
with open("input.txt") as file:
    lines = file.readlines()
    moveTail(head, head.nextNode)
    for line in lines:
        COMMANDS[line[0]](head, int(line.split(' ')[1]))
print(len(tail1.tailWasHere))
print(len(tail2.tailWasHere))
print(len(tail3.tailWasHere))
print(len(tail4.tailWasHere))
print(len(tail5.tailWasHere))
print(len(tail6.tailWasHere))
print(len(tail7.tailWasHere))
print(len(tail8.tailWasHere))
print(len(tail9.tailWasHere))
