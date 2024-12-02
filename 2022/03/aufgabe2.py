import string

STATIC_ALPHABET = ' ' + string.ascii_lowercase + string.ascii_uppercase

with open("input.txt") as file:
    backpacks = file.readlines()
    groups =[]
    counter = 0
    while counter < len(backpacks):
        groups.append(backpacks[counter:counter+3])
        counter+=3

    batches =[]
    for group in groups:
        batch=''
        for item in group[0].strip():
            if group[1].__contains__(item):
                if group[2].__contains__(item):
                    batch=item
        batches.append(batch)
    sum=0
    for batch in batches:
        sum += STATIC_ALPHABET.index(batch)
    print(sum)
