def treeIsVisible(treeToSee, forest):
    for tree in forest:
        if treeToSee <= tree:
            return False
    return True


def howFarCanISee(treeToSee, forest):
    if forest == []:
        return 1
    sum = 0
    for tree in forest:
        if treeToSee > tree:
            sum += 1
        elif treeToSee <= tree:
            return sum + 1
        else:
            return sum
    return sum


def isOutline(rowIdx, columnIdx, grid):
    return rowIdx == 0 or \
           rowIdx == len(grid) or \
           columnIdx == 0 or \
           columnIdx == len(grid[0])


with open("input.txt") as file:
    lines = file.readlines()
    dim_columns = len(lines[0])
    dim_row = len(lines)
    grid = [[0 for x in range(dim_columns - 1)] for i in range(dim_row)]

    lineCounter = 0
    for line in lines:
        charCounter = 0
        string = line.replace('\n', '')
        for c in string:
            grid[lineCounter][charCounter] = int(c)
            charCounter += 1
        lineCounter += 1

    counter = 0
    rowIdx = 0
    treeScoreArray = []
    for row in grid:
        colIdx = 0
        visible = False
        for column in grid:
            if treeIsVisible(grid[rowIdx][colIdx], grid[rowIdx][0:colIdx]) or \
                    treeIsVisible(grid[rowIdx][colIdx], grid[rowIdx][colIdx + 1::]) or \
                    treeIsVisible(grid[rowIdx][colIdx], [i[colIdx] for i in grid[0:rowIdx]]) or \
                    treeIsVisible(grid[rowIdx][colIdx], [i[colIdx] for i in grid[rowIdx + 1::]]):
                counter += 1
            treeScore = 1
            treeScore *= howFarCanISee(grid[rowIdx][colIdx], grid[rowIdx][0:colIdx][::-1])
            treeScore *= howFarCanISee(grid[rowIdx][colIdx], grid[rowIdx][colIdx + 1::])
            treeScore *= howFarCanISee(grid[rowIdx][colIdx], [i[colIdx] for i in grid[0:rowIdx]][::-1])
            treeScore *= howFarCanISee(grid[rowIdx][colIdx], [i[colIdx] for i in grid[rowIdx + 1::]])
            treeScoreArray.append(treeScore)

            if treeScore == 16:
                print(grid[rowIdx][colIdx])
                print(howFarCanISee(grid[rowIdx][colIdx], grid[rowIdx][0:colIdx][::-1]))
                print(howFarCanISee(grid[rowIdx][colIdx], grid[rowIdx][colIdx + 1::]))
                print(howFarCanISee(grid[rowIdx][colIdx], [i[colIdx] for i in grid[0:rowIdx]][::-1]))
                print(howFarCanISee(grid[rowIdx][colIdx], [i[colIdx] for i in grid[rowIdx + 1::]]))
            colIdx += 1

        rowIdx += 1

print(counter)
print(max(treeScoreArray))
