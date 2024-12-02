dividierenDurch = [7, 13, 5, 11]
for i in range(0, 10000000000):
    if i % 7 == 0 \
            and i % 13 == 0 \
            and i % 5 == 0 \
            and i % 11 == 0 \
            and i % 19 == 0 \
            and i % 2 == 0 \
            and i % 3 == 0 \
            and i % 17 == 0:
        print(i)
