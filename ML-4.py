
grid = open("test4.txt").read().splitlines()

print('grid', grid)

rows = len(grid)
cols = len(grid[0])

# PART - 1
def get_score(row, column):
    result = 0
    for dr in (1, 0, -1):
        for dc in (1, 0, -1):
            if dr == dc == 0:
                continue

            for i in range(len('XMAS')):
                nr = row + dr * i
                nc = column + dc * i

                if 0<= nr < rows and  0<= nc < cols:
                    if grid[nr][nc] == 'XMAS'[i]:
                        if i == 3:
                            result += 1
                    else:
                        break
    return result

# Part 2

def isContainsWord(row1, column1, dc):
    word = ''

    for i in range(len('MAS')):
        nr = row1 + i
        nc = column1 + dc * i

        if 0 <= nr < rows and 0 <= nc < cols:
            if grid[nr][nc] == 'MAS'[i] or grid[nr][nc] == 'SAM'[i]:
                word += grid[nr][nc]

                if i == 2 and (word == 'MAS' or word == 'SAM'):
                    return True
    return False


def get_score2(r, col):
    result = 0
    isOneDiagonalTrue = isContainsWord(r, col,1)
    if isOneDiagonalTrue:
        newColumn = col + 2
        isSecondDiagonalTrue = isContainsWord(r, newColumn, -1)
        if isSecondDiagonalTrue:
            result += 1

    return result

total = 0
for row in range(rows):
    for column in range(cols):
        # total += get_score(row, column)
        total += get_score2(row, column)
print('total', total)