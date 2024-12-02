def replaceWritenNums(str):
    str = str.replace('oneight', 'oneeight')
    str = str.replace('twone', 'twoone')
    str = str.replace('threeight', 'threeeight')
    str = str.replace('fiveight', 'fiveeight')
    str = str.replace('sevenine', 'sevennine')
    str = str.replace('eightwo', 'eighttwo')
    str = str.replace('eighthree', 'eightthree')
    str = str.replace('nineight', 'nineeight')
    str = str.replace('oneight', 'oneeight')

    str = str.replace('one', '1')
    str = str.replace('two', '2')
    str = str.replace('three', '3')
    str = str.replace('four', '4')
    str = str.replace('five', '5')
    str = str.replace('six', '6')
    str = str.replace('seven', '7')
    str = str.replace('eight', '8')
    str = str.replace('nine', '9')
    return str


# Using readlines()
file1 = open('input.txt', 'r')
lines = file1.readlines()

sum = 0
for line in lines:
    print(line)
    line = replaceWritenNums(line)
    res = [int(i) for i in list(line) if i.isdigit()]
    print(res)
    sum += int(str(res[0]) + str(res[-1]))
print(sum)

