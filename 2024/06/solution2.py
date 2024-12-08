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

global loop_count
loop_count=0
def search_loop(map):
    global loop_count
    map = copy(map)
    c = current_pos(find_player(map), map)
    n = move_turn[find_player(map)](c)
    np = find_player(map)
    np = turn_player[np]
    map = map[: c] + 'X' + map[c + 1:]
    map = map[: n] + np + map[n + 1:]
    while True:
        c = current_pos(find_player(map), map)
        n = move_straight[find_player(map)](c)
        np = find_player(map)
        if map[n] == '*':
            break
        if str(c)+map[c] in cord_dir_dict:
            loop_count+=1
            break
        if map[n] == '#':
            n = move_turn[find_player(map)](c)
            np = turn_player[np]
        map = map[: c] + 'X' + map[c + 1:]
        map = map[: n] + np + map[n + 1:]

cord_dir_dict={}
count=0
while True:
    count+=1
    print(count,loop_count)
    c = current_pos(find_player(map), map)
    cord_dir_dict[str(c)+map[c]]=0
    n = move_straight[find_player(map)](c)
    np = find_player(map)
    search_loop(map)
    if map[n] == '*':
        break
    if map[n] == '#':
        n = move_turn[find_player(map)](c)
        np = turn_player[np]
    map = map[: c] + 'X' + map[c + 1:]
    map = map[: n] + np + map[n + 1:]
print(map.count('X'))
