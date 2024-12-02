
with open("input.txt") as file:
    lines = file.readlines()
    ids=[]
    for line in lines:
        for string in line.strip().split(','):
            for n in string.split('-'):
                ids.append(id(n))
ids = list(dict.fromkeys(ids))
print(len(ids))


print('07'<='17')
print('7'<='17')