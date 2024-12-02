def calc_dist_score(left, right):
    distance = 0
    left.sort()
    right.sort()
    for l, r in zip(left, right):
        distance += abs(l - r)
    print('Distance is ', distance)


def calc_sim_score(left, right):
    sim_score = 0
    for l in left:
        sim_score += l * right.count(l)
    print('The similarity score is', sim_score)


left,right = [],[]
with open('input.txt', 'r') as file:
    for line in file:
        if len(line) > 2:
            split = line.split("   ")
            left.append(int(split[0].strip()))
            right.append(int(split[1].strip()))

calc_dist_score(left, right)
calc_sim_score(left, right)
