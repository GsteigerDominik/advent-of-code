def extract_number(array):
    if len(array) == 1:
        return array[0]
    elif len(array) == 2:
        return array[0] * 10 + array[1]

# Using readlines()
file1 = open('input.txt', 'r')
lines = file1.readlines()

MAX_GREEN=13
MAX_RED=12
MAX_BLUE=14
total_ids=0

for line in lines:
    gameIsPossible= True
    id = extract_number([int(i) for i in list(line.split(':')[0]) if i.isdigit()])
    sets = line.split(':')[1].split(';')
    for set in sets:
        singleRecords = set.split(',')
        for singleRecord in singleRecords:
           num = extract_number([int(i) for i in list(singleRecord) if i.isdigit()])
           if "green" in singleRecord and MAX_GREEN < num:
               gameIsPossible = False
           elif "blue" in singleRecord and MAX_BLUE < num:
               gameIsPossible = False
           elif "red" in singleRecord and MAX_RED < num:
               gameIsPossible = False
    if gameIsPossible:
        total_ids +=id
print(total_ids)