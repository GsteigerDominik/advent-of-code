import pprint as pp
def compare(left, right):
    pp.pprint('Comparing')
    pp.pprint(left)
    pp.pprint(right)
    if isinstance(left, int) and isinstance(right, int):
        return left < right
    elif isinstance(left,list) and isinstance(right,list):
        try:
            length=len(left) if len(left) > len(right) else len(right)
            for i in range(length):
                if compare(left[i], right[i]):
                    return True
                if left[i] > right[i]:
                    return False
                if i == length-1 and left[i] == right[i]:
                    return True
        except:
            return len(left) < len(right)
        return False
    elif isinstance(left,list):
        return compare(left, [right])
    elif isinstance(right,list):
        return compare([left], right)


with open("input.txt") as file:
    lines = file.readlines()

    pairs = []
    pairs.append([])
    for line in lines:
        if line == '\n':
            pairs.append([])
        else:
            pairs[-1].append(eval(line.strip()))
    sum = 0
    for pair in pairs:
        left = pair[0]
        right = pair[1]
        result=compare(left, right)
        print(pairs.index(pair) + 1, result)
        if result:
            sum += pairs.index(pair) + 1
    print(sum)
