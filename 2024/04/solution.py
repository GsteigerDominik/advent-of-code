from pprint import pprint

with open('input.txt', 'r') as file:
    array = []
    for line in file:
        array.append("#"+line.strip()+"#")
    first_last= ""
    for c in range(0,len(array[0])):
        first_last += '#'
    array.insert(0,first_last)
    array.append(first_last)
full_text_string = "".join(array)
pprint(array)
print(full_text_string)

LEN= len(array[0])
HEI= len(array)
print('Len:',LEN,'HEI',HEI)


in_bounds= lambda x:0 < x <(LEN*HEI)
lambda_array = [
    lambda x: x+1, #Horizontal 1
    lambda x: x-1, #Horizontal 2
    lambda x: x+LEN, #Vertical 1
    lambda x: x-LEN, #Vertical 2
    lambda x: x + LEN + 1, #Diag 1
    lambda x: x + LEN - 1, #Diag 2
    lambda x: x - LEN + 1, #Diag 3
    lambda x: x - LEN - 1, #Diag 4
]
count = 0
for x in [idx for idx, c in enumerate(full_text_string) if c == 'X']: # FOR EACH X
    for l in [l for l in lambda_array if in_bounds(l(x)) and full_text_string[l(x)] == 'M']:
        m =l(x)
        if 0<l(m)<(LEN*HEI) and full_text_string[l(m)] == 'A':
            a =l(m)
            if 0<l(a)<(LEN*HEI) and full_text_string[l(a)] == 'S':
                count +=1
print(count)

# Part 2


lambda_array_part2 = [
    # oben
    lambda x: [x + LEN + 1,x + LEN - 1,x - LEN + 1,x - LEN - 1], #UNTEN / OBEN
    lambda x: [x + LEN + 1,x - LEN + 1,x + LEN - 1,x - LEN - 1], #RECHTS / LINKS
    lambda x: [x - LEN + 1,x - LEN - 1,x + LEN + 1,x + LEN - 1], #OBEN / UNTEN
    lambda x: [x + LEN - 1,x - LEN - 1,x + LEN + 1,x - LEN + 1] #LINKS / RECHTS
]
count = 0
for a in [idx for idx, c in enumerate(full_text_string) if c == 'A']:
    for l in [l for l in lambda_array_part2 if in_bounds(l(a)[0])
                                               and in_bounds(l(a)[1])
                                               and full_text_string[l(a)[0]] == 'M'
                                               and full_text_string[l(a)[1]] == 'M'
                                               and full_text_string[l(a)[2]] == 'S'
                                               and full_text_string[l(a)[3]] == 'S']:
        count += 1
print('Results:',count)