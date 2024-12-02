def endCicle(param):
    global CYCLES
    CYCLES.append(X)


def addX(param):
    global CYCLES
    global X
    CYCLES.append(X)
    CYCLES.append(X)
    X += int(param)


COMMANDS = {
    'noop': endCicle,
    'addx': addX,
}
CYCLES = []
X = 1
with open("input.txt") as file:
    lines = file.readlines()
    for line in lines:
        param = line.strip().split(' ')[1] if len(line.strip().split(' ')) >= 2 else None
        COMMANDS[line.strip().split(' ')[0]](param)
interestingCycles = [20, 60, 100, 140, 180, 220]
total = 0
for cycle in interestingCycles:
    total += cycle * CYCLES[cycle - 1]

print('Total', total)
print(len(CYCLES))
index = 0
CRT = []
for line in range(6):
    CRT.append([])
    for pixel in range(40):
        x=CYCLES[pixel + (line * 40)]
        sprite = range(x-1, x+2, 1)
        if pixel in sprite:
            CRT[line].append('#')
        else:
            CRT[line].append('.')
print(''.join(CRT[0]))
print(''.join(CRT[1]))
print(''.join(CRT[2]))
print(''.join(CRT[3]))
print(''.join(CRT[4]))
print(''.join(CRT[5]))
ECZUZALR