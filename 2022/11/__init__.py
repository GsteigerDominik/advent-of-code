import math


class Monkey:

    def __init__(self):
        self.items = []
        self.operation = None
        self.test = None
        self.inspectedItems = 0


def createNewMonkey(line, monkey):
    print(line)


def addStartingItems(line, monkey):
    print(line)


def addOperation(line, monkey):
    print(line)


def addTest(line, monkey):
    print(line)


def addIfTrue(line, monkey):
    print(line)


def addIfFalse(line, monkey):
    print(line)


def throwToMonkey(num):
    return num


COMMANDS = {
    'Monkey': createNewMonkey,
    '  Starting items:': addStartingItems,
    '  Operation:': addOperation,
    '  Test:': addTest,
    '    If true:': addIfTrue,
    '    If false:': addIfFalse,
}


# monkey1 = Monkey([79, 98], lambda x: x * 19, lambda x: throwToMonkey(2) if x % 23 == 0 else throwToMonkey(3))
# monkey1.test(46)
def readFile():
    monkeys = []
    with open("input.txt") as file:
        lines = file.readlines()
    tempDivisibleNr = -1
    tempTrueThrow = -1
    tempFalseThrow = -1
    for line in lines:
        if line.startswith('Monkey'):
            monkeys.append(Monkey())
            tempDivisibleNr = -1
            tempTrueThrow = -1
            tempFalseThrow = -1
        elif line.startswith('  Starting items:'):
            items = [int(x) for x in line.split(':')[1].strip().replace(' ', '').split(',')]
            monkeys[-1].items = items
        elif line.startswith('  Operation:'):
            string = line.split('=')[1].strip().replace(' ', '')
            monkeys[-1].operation = eval('lambda old: ' + string)
        elif line.startswith('  Test:'):
            tempDivisibleNr = int(line.split('by')[1].strip())
        elif line.startswith('    If true:'):
            tempTrueThrow = int(line.split('monkey')[1].strip())
        elif line.startswith('    If false:'):
            tempFalseThrow = int(line.split('monkey')[1].strip())
        elif line.__eq__('\n'):
            monkeys[-1].test = eval(str('lambda x: throwToMonkey(' + str(tempTrueThrow) +
                                        ') if x % ' + str(tempDivisibleNr) +
                                        ' == 0 else throwToMonkey(' + str(tempFalseThrow) + ')'))
    return monkeys


monkeys = readFile()

rounds = 20
#rounds = 10000
for r in range(0, rounds):
    for monkey in monkeys:
        for item in monkey.items:
            monkey.inspectedItems += 1
            # item = math.floor(monkey.operation(item) % 9699690)
            item = math.floor(monkey.operation(item) / 3)
            monkeyToGetItem = monkey.test(item)
            monkeys[monkeyToGetItem].items.append(item)
        monkey.items = []
monkeyBusiness = []
for monkey in monkeys:
    monkeyBusiness.append(monkey.inspectedItems)
monkeyBusiness.sort()
print(monkeyBusiness[-1], monkeyBusiness[-2])
print(monkeyBusiness[-1] * monkeyBusiness[-2])
