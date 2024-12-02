# [D]
# [N] [C]
# [Z] [M] [P]
# 1   2   3

#ladeFlaeche = {
#    "1": ['Z', 'N'],
##    "2": ['M', 'C', 'D'],
#        "3": ['P']
#}
ladeFlaeche = {
    "1": ['T', 'P', 'Z', 'C', 'S', 'L', 'Q', 'N'],
    "2": ['L', 'P', 'T', 'V', 'H', 'C', 'G'],
    "3": ['D', 'C', 'Z', 'F'],
    "4": ['G', 'W', 'T', 'D', 'L', 'M', 'V', 'C'],
    "5": ['P', 'W', 'C'],
    "6": ['P', 'F', 'J', 'D', 'C', 'T', 'S', 'Z'],
    "7": ['V', 'W', 'G', 'B', 'D'],
    "8": ['N', 'J', 'S', 'Q', 'H', 'W'],
    "9": ['R', 'C', 'Q', 'F', 'S', 'L', 'V']
}
def getResultFromLadeFlaeche():
    result = ''
    for key in ladeFlaeche:
        result += ladeFlaeche.get(key)[-1]
    return result

with open("input.txt") as file:
    lines = file.readlines()
    for line in lines:
        words = line.split()
        index = len(ladeFlaeche.get(words[3])) - int(words[1])
        print(words[1],index, ladeFlaeche.get(words[3]))
        for i in range(int(words[1])):
            #Lösung 1ladeFlaeche.get(words[5]).append(ladeFlaeche.get(words[3]).pop(-1))
            ladeFlaeche.get(words[5]).append(ladeFlaeche.get(words[3]).pop(index))
    print(getResultFromLadeFlaeche()) #Works fine
    # move 1 from 2 to 1

#Learning remove uses actual vale and not index....