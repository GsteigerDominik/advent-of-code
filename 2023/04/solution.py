from pprint import pprint

file1 = open('input.txt', 'r')
lines = file1.readlines()
cards = []

for line in lines:
    #Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    card = []
    inhalt = line.split(":")[1]
    num_lists= inhalt.split("|")
    for num_list in num_lists:
        num_list=num_list.strip()
        res = [int(i) for i in num_list.split(" ") if i.isdigit()]
        card.append(res)
    cards.append(card)

sum=0
for card in cards:
    points=0
    for num in card[1]:
        if card[0].__contains__(num):
            if points==0:
                points=1
            else:
                points*=2
    sum += points
print(sum)