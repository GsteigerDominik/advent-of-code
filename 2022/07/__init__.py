directories = {}
currentDirectory = ''
commandCd = '$ cd'
commandLs = '$ ls'
lsDir = {}


def getAndCreateDirFromString(string):
    temp = directories
    for directory in list(filter(None, string.split('/'))):
        if temp.get(directory) is None:
            temp[directory] = {}
        else:
            temp = temp.get(directory)
    return temp


dicSizes = []


def getSizeOfDir(directory):
    sum = 0
    for value in directory.values():
        if type(value) is dict:
            sum += getSizeOfDir(value)
        else:
            sum += value
    dicSizes.append(sum)
    return sum


with open("input.txt") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        if line.startswith(commandCd):
            if line.__eq__(commandCd + ' /'):
                currentDirectory = '/'
            elif line.__eq__(commandCd + ' ..'):
                if currentDirectory != '/':
                    currentDirectory = '/'.join(currentDirectory.split('/')[0:-2]) + '/'
            else:
                currentDirectory = currentDirectory + line.removeprefix(commandCd).strip() + '/'
                getAndCreateDirFromString(currentDirectory)
        else:
            if not line.startswith(commandLs):
                if line.startswith('dir '):
                    print('not relevant right now')
                else:
                    getAndCreateDirFromString(currentDirectory)[line.split(' ')[1]] = int(line.split(' ')[0])
print(getSizeOfDir(directories))
total = 0
for size in dicSizes:
    if size < 100000:
        total += size
enoghBigFolder = []
freeSpace = 70000000 - max(dicSizes)
neededSpace = 30000000-freeSpace
for size in dicSizes:
    if size >= neededSpace:
        enoghBigFolder.append(size)
print('freeSpace ', freeSpace)
print('neededSpace ', neededSpace)
print('enoghBigFolder ', enoghBigFolder)
print('min ', min(enoghBigFolder))
