import string
STATIC_ALPHABET =' '+string.ascii_lowercase+string.ascii_uppercase

with open("input.txt") as file:
    wrongItems=[]
    backpacks = file.readlines()
    for backpack in backpacks:
        backpack = backpack.strip()
        compartmentOne =backpack[:len(backpack)//2]
        compartmentTwo =backpack[len(backpack)//2:]
        wrongItem=''
        for item in compartmentOne:
            if compartmentTwo.__contains__(item):
                wrongItem=item
        wrongItems.append(wrongItem)

    sum=0
    for item in wrongItems:
        sum += STATIC_ALPHABET.index(item)
    print(sum)