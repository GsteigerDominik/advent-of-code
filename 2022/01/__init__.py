# Using readlines()
file1 = open('input.txt', 'r')
Lines = file1.readlines()

count = 0
countElfen=0
summe =0
data= {}
# Strips the newline character
lastWasBlank = False
for line in Lines:
    if lastWasBlank:
        lastWasBlank = False
        data[countElfen] = summe
        summe = 0
    if line.strip() == '':
        countElfen += 1
        lastWasBlank = True
    else:
        summe += int(line.strip())
print(max(data.values()))

list=list(data.values())

print(sum(sorted(list,reverse=True)[:3]))