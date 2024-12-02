def isOneIncludedInOther(firstElf, secondElf):
    return (int(firstElf[0]) <= int(secondElf[0]) and int(firstElf[1]) >= int(secondElf[1])) or \
           (int(secondElf[0]) <= int(firstElf[0]) and int(secondElf[1]) >= int(firstElf[1]))


def isOneIncludedInOtherString(firstElf, secondElf):
    return (firstElf[0] <= secondElf[0] and firstElf[1] >= secondElf[1]) or \
           (secondElf[0] <= firstElf[0] and secondElf[1] >= firstElf[1])


with open("input.txt") as file:
    lines = file.readlines()
    pairs = []
    for line in lines:
        sections = []
        for string in line.split(','):
            sections.append(string.replace('\n', ''))
        pairs.append(sections)

    fullRedundant = 0
    fullRedundantStrings = 0
    notSameIntAndString = 0
    for pair in pairs:
        firstElf = pair[0].split('-')
        secondElf = pair[1].split('-')
        if isOneIncludedInOther(firstElf, secondElf):
            fullRedundant += 1
        if isOneIncludedInOtherString(firstElf, secondElf):
            fullRedundantStrings += 1
        if isOneIncludedInOtherString(firstElf, secondElf) and not isOneIncludedInOther(    firstElf, secondElf):
            notSameIntAndString += 1
            #es muss noch ein zweiter string geben der auf das zeigt.....
            print(isOneIncludedInOtherString(firstElf,secondElf),
                  isOneIncludedInOther(firstElf,secondElf),
                  id(firstElf[0]),
                  id(firstElf[1]),
                  id(secondElf[0]),
                  id(secondElf[1]))
    print(fullRedundant)
    print(fullRedundantStrings)
    print(notSameIntAndString)
