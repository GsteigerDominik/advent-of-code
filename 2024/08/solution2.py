from itertools import combinations
from pprint import pprint

map = ''
LEN = 0
with open('input.txt', 'r') as file:
    map_array = []
    side='****************************************************************************************************'
    for line in file:
        map_array.append(side+line.strip()+side)
    LEN = len(map_array[0])
    map = ''.join(map_array)
    top = side+side
    for i in range(0,LEN):
        top += '*'
    for i in range(0, 100):
       map = top + map + top

char_coord_dict = {}
for idx,char in enumerate(map):
    if char not in ('*','.','#'):
        if char not in char_coord_dict:
            char_coord_dict[char] = [idx]
        else:
            char_coord_dict[char].append(idx)
pprint(char_coord_dict)
write = lambda text,idx,ins: text[: idx] + ins+ text[idx + 1:]
for char,coords in char_coord_dict.items():
    for comb in list(combinations(coords, 2)):
        for i in range(1,100):
            pos1= min(comb) - abs(comb[0] - comb[1])*i
            pos2= max(comb) + abs(comb[0] - comb[1])*i
            map = write(map,pos1,char) if 0 < pos1 < len(map) and map[pos1] not in ('*') else map
            map = write(map,pos2,char) if 0 < pos2 < len(map) and map[pos2] not in ('*') else map
n = LEN
out = [(map[i:i + n]) for i in range(0, len(map), n)]
pprint(out)


char_coord_dict = {}
for idx,char in enumerate(map):
    if char not in ('*','.','#'):
        if char not in char_coord_dict:
            char_coord_dict[char] = [idx]
        else:
            char_coord_dict[char].append(idx)
for char,coords in char_coord_dict.items():
    for comb in list(combinations(coords, 2)):
        map =write(map,min(comb)-abs(comb[0]-comb[1]),'#') if 0 < min(comb)-abs(comb[0]-comb[1]) < len(map) and map[min(comb)-abs(comb[0]-comb[1])] not in ('*') else map
        map =write(map,max(comb)+abs(comb[0]-comb[1]),'#') if 0 < max(comb)+abs(comb[0]-comb[1]) < len(map) and map[max(comb)+abs(comb[0]-comb[1])] not in ('*') else map
print(map.count('#'))

n = LEN
out = [(map[i:i + n]) for i in range(0, len(map), n)]
pprint(out)