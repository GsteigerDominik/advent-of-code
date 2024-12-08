from copy import copy
from itertools import combinations_with_replacement, product
from pprint import pprint

equations = []
with open('input.txt', 'r') as file:
    for line in file:
        result, nums = line.strip().split(":")
        equations.append((int(result), [int(num) for num in nums.split(" ") if num != '']))

# 0 11, + 6, + 16, + 20
# 1 11, * 6, + 16, + 20
# 2 11, + 6, * 16, + 20
# 3 11, + 6, + 16, * 20
# 4 11, * 6, * 16, + 20
# 5 11, + 6, * 16, * 20
# 6 11, * 6, + 16, * 20
# 7 11, * 6, + 16, * 20
calc = {
    '*': lambda x,y: x*y,
    '+': lambda x,y: x+y,
    '||': lambda x,y: int(str(x)+str(y)),
}

print(equations)
total = 0
for idx,equation in enumerate(equations):

    combinations = product (['+','*','||'], repeat=len(equation[1]) - 1)
    valid = False
    for comb in list(combinations):

        tmp_term =  copy(equation[1])
        for i,c in enumerate(comb):
            tmp_term.insert(i+i+1,c)

        for x in range(0, int((len(tmp_term)-1)/2)):
            term1 =tmp_term.pop(0)
            zeichen =tmp_term.pop(0)
            term2 =tmp_term.pop(0)
            result = calc[zeichen](term1,term2)
            tmp_term.insert(0,result)
        if tmp_term[0] == equation[0]:
            valid= True
            break
    if valid:
        total += equation[0]
    print(idx,' of ',len(equations))
print(total)
