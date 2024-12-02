def getAllNumbersFromRange(range):
    nums= range.split('-')
    value=[]
    counter= int(nums[0])
    while counter <= int(nums[1]):
        value.append(counter)
        counter+=1
    return value
def getTupleFromRange(range):
    nums= range.split('-')
    return [int(nums[0]),int(nums[1])]

with open("input.txt") as file:
    lines = file.readlines()
    pairs = []
    for line in lines:
        sections = []
        for string in line.split(','):
            sections.append(string.replace('\n', ''))
        pairs.append(sections)

    fullRedundant = 0
    overlapping = 0
    for pair in pairs:
        firstElf = pair[0]
        secondElf = pair[1]
        if (getAllNumbersFromRange(firstElf).__contains__(getTupleFromRange(secondElf)[0]) and\
                getAllNumbersFromRange(firstElf).__contains__(getTupleFromRange(secondElf)[1])) or\
            (getAllNumbersFromRange(secondElf).__contains__(getTupleFromRange(firstElf)[0]) and \
             getAllNumbersFromRange(secondElf).__contains__(getTupleFromRange(firstElf)[1])) :
            fullRedundant+=1
        if getAllNumbersFromRange(firstElf).__contains__(getTupleFromRange(secondElf)[0]) or \
            getAllNumbersFromRange(firstElf).__contains__(getTupleFromRange(secondElf)[1]) or \
            getAllNumbersFromRange(secondElf).__contains__(getTupleFromRange(firstElf)[0]) or \
            getAllNumbersFromRange(secondElf).__contains__(getTupleFromRange(firstElf)[1]) :
            overlapping+=1
    print(fullRedundant)
    print(overlapping)
