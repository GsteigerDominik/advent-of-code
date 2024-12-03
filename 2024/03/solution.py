import re


def mul(lines):
    result = 0
    for line in lines:
        instructions = re.findall("mul\([0-9]*,[0-9]*\)", line)
        for instruction in instructions:
            params = [int(s) for s in re.findall('\d+', instruction)]
            result += params[0] * params[1]
    return result


def mul_do_dont(lines):
    mul_enabled = True
    result = 0
    for line in lines:
        instructions = re.findall("mul\([0-9]*,[0-9]*\)|do\(\)|don\'t\(\)", line)
        for instruction in instructions:
            if instruction == 'do()':
                mul_enabled = True
            elif instruction == "don't()":
                mul_enabled = False
            elif mul_enabled:
                params = [int(s) for s in re.findall('\d+', instruction)]
                result += params[0] * params[1]
    return result


with (open('input.txt', 'r') as file):
    print(mul(file))
with (open('input.txt', 'r') as file):
    print(mul_do_dont(file))
