def extract_number(array):
    if len(array) == 1:
        return array[0]
    elif len(array) == 2:
        return array[0] * 10 + array[1]

# Using readlines()
file1 = open('input.txt', 'r')
lines = file1.readlines()


total_sum=0

for line in lines:
    id = extract_number([int(i) for i in list(line.split(':')[0]) if i.isdigit()])
    sets = line.split(':')[1].split(';')
    MAX_GREEN=0
    MAX_RED=0
    MAX_BLUE=0
    for set in sets:
        singleRecords = set.split(',')
        for singleRecord in singleRecords:
           num = extract_number([int(i) for i in list(singleRecord) if i.isdigit()])
           if "green" in singleRecord and MAX_GREEN < num:
               MAX_GREEN = num
           elif "blue" in singleRecord and MAX_BLUE < num:
               MAX_BLUE = num
           elif "red" in singleRecord and MAX_RED < num:
               MAX_RED = num
    total_sum += MAX_BLUE*MAX_RED*MAX_GREEN
print(total_sum)