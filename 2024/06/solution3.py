from copy import copy
from pprint import pprint

map = ''
LEN = 0
with open('input.txt', 'r') as file:
    map_array = []
    for line in file:
        map_array.append('*' + line.strip() + '*')
    first_last = ''
    for c in range(0, len(map_array[0])):
        first_last += '*'
    map_array.insert(0, first_last)
    map_array.append(first_last)
    LEN = len(map_array[0])
    map = ''.join(map_array)

print(LEN)
print(map)

lambda_array = [
    lambda x: x + 1,  # DOWN
    lambda x: x - 1,  # UP
    lambda x: x + LEN,  #
    lambda x: x - LEN,  # Vertical 2
]
# ^ > v <
move_straight = {
    ">": lambda x: x + 1,
    "<": lambda x: x - 1,
    "v": lambda x: x + LEN,
    "^": lambda x: x - LEN
}

move_turn = {
    ">": lambda x: x + LEN,
    "<": lambda x: x - LEN,
    "v": lambda x: x - 1,
    "^": lambda x: x + 1
}

turn_player = {
    ">": "v",
    "<": "^",
    "v": "<",
    "^": ">"
}


def find_player(map):
    found_chars = [char for char in map if char in {'>', '<', 'v', '^'}]
    return found_chars[0] if len(found_chars) == 1 else None


def current_pos(player, map):
    return map.index(player)


print(find_player(map))

c = current_pos(find_player(map), map)
print(c)
print(move_straight[find_player(map)](c))

#prepare stupid array
def prepare_array(map):
    visit_pos = []
    while True:
        c = current_pos(find_player(map), map)
        visit_pos.append(str(c)+map[c])
        n = move_straight[find_player(map)](c)
        np = find_player(map)
        if map[n] == '*':
            break
        if map[n] == '#':
            n = move_turn[find_player(map)](c)
            np = turn_player[np]
        map = map[: c] + 'X' + map[c + 1:]
        map = map[: n] + np + map[n + 1:]
    return visit_pos
count_loops =0
def try_right(map1):
    global count_loops
    map=copy(map1)
    c = current_pos(find_player(map), map)
    obs = move_straight[find_player(map)](c)
    map = map[: obs] + '#' + map[obs + 1:]
    n = move_turn[find_player(map)](c)
    np = find_player(map)
    np = turn_player[np]
    map = map[: c] + 'X' + map[c + 1:]
    map = map[: n] + np + map[n + 1:]
    count= 0
    edges = 0
    while True:
        count+=1
        c = current_pos(find_player(map), map)
        if str(c) + map[c] in visit_pos:
            count_loops += 1
            break
        n = move_straight[find_player(map)](c)
        np = find_player(map)
        if map[n] == '*' or count > 5000 or edges > 3:
            break
        if map[n] == '#':
            edges+= 1
            n = move_turn[find_player(map)](c)
            np = turn_player[np]
        map = map[: c] + 'X' + map[c + 1:]
        map = map[: n] + np + map[n + 1:]

print('prep array')
visit_pos = prepare_array(map)
print('prep array fintioo')
count =0
while True:
    count+= 1
    print(count)
    c = current_pos(find_player(map), map)
    visit_pos.append(str(c)+map[c])
    try_right(map)
    n = move_straight[find_player(map)](c)
    np = find_player(map)
    if map[n] == '*':
        break
    if map[n] == '#':
        n = move_turn[find_player(map)](c)
        np = turn_player[np]
    map = map[: c] + 'X' + map[c + 1:]
    map = map[: n] + np + map[n + 1:]
print(map.count('X')+1)
print('CountLoops',count_loops)