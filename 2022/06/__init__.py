def double_letters(string):
    return len(set(string)) != len(string)

def recursiveSearch(index, string):
    if not double_letters(string[index:index+4]):
        return index
    return recursiveSearch(index+1,string)

def recursiveSearchPart2(index, string):
    if not double_letters(string[index:index+14]):
        return index
    return recursiveSearchPart2(index+1,string)

import sys
#Part 1
#with open("input.txt") as file:
#    lines = file.readlines()
#    for line in lines:
#        sys.setrecursionlimit(len(line))
#        i=recursiveSearch(0,line)
#        print(i+4)

with open("input.txt") as file:
    lines = file.readlines()
    for line in lines:
        index=0
        for char in line:
            if not double_letters(line[index:index+14]):
                print(index+14)
                break
            index+=1
        #sys.setrecursionlimit(len(line))
        #print(sys.getrecursionlimit())
        #i=recursiveSearchPart2(0,line)
        #print(i+14)