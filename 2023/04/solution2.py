from pprint import pprint

file1 = open('input.txt', 'r')
lines = file1.readlines()
cards = []

for line in lines:
    #Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    card = []
    card.append(line.split(":")[0])
    inhalt = line.split(":")[1]
    num_lists= inhalt.split("|")
    for num_list in num_lists:
        num_list=num_list.strip()
        res = [int(i) for i in num_list.split(" ") if i.isdigit()]
        card.append(res)
    cards.append(card)

for i in range(0,len(cards)):
    card = cards[i]
    pointer = i+1
    for num in card[2]:
        if card[1].__contains__(num) and pointer in range(0,len(cards)):
            print(pointer)
            cards.insert(pointer,cards[pointer])
            pointer+=1
pprint(cards)