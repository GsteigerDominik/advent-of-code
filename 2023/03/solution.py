from pprint import pprint

file1 = open('input.txt', 'r')
lines = file1.readlines()
engine = []

for line in lines:
    e_line = []
    for char in line:
        if char != '\n':
            e_line.append(char)
    engine.append(e_line)


def remove_nums_dots(string):
    new_string = ""
    for char in list(string):
        if not char.isdigit() and not char == '.':
            new_string += char
    return new_string


def get_block_if_in_engine(x, y, engine):
    if 0 <= x < len(engine) and 0 <= y < len(engine[0]):
        return engine[x][y]
    return '.'


def check_surrounding(x, y, engine):
    surrounding = ""
    surrounding += get_block_if_in_engine(x - 1, y - 1, engine)
    surrounding += get_block_if_in_engine(x - 1, y, engine)
    surrounding += get_block_if_in_engine(x - 1, y + 1, engine)

    surrounding += get_block_if_in_engine(x, y - 1, engine)
    surrounding += get_block_if_in_engine(x, y, engine)
    surrounding += get_block_if_in_engine(x, y + 1, engine)

    surrounding += get_block_if_in_engine(x + 1, y - 1, engine)
    surrounding += get_block_if_in_engine(x + 1, y, engine)
    surrounding += get_block_if_in_engine(x + 1, y + 1, engine)

    surrounding = remove_nums_dots(surrounding)
    if len(surrounding) > 0:
        return True
    return False


sum = 0
for x in range(len(engine)):
    detected_number = False
    number_is_connected = False
    number = ""
    for y in range(len(engine[x])):
        if engine[x][y].isdigit():
            number += engine[x][y]
            detected_number = True
        else:
            if len(number) > 0:
                if number_is_connected:
                    sum += int(number)
                detected_number = False
                number_is_connected = False
                number = ""
        if detected_number:
            if check_surrounding(x, y, engine):
                number_is_connected = True
        if y == len(engine[x])-1 and engine[x][y].isdigit():
            print(number)
            if number_is_connected:
                sum += int(number)
print(sum)
