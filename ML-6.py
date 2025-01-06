up = '^'
right = '>'
left = '<'
down = 'v'
obstruction = '#'

map = open('test6.txt').read().splitlines()
rowCount = len(map)
columnCount = len(map[0])


def findPositionOfGuard():
    for row in range(rowCount):
        for column in range(columnCount):
            if map[row][column] == up:
                return (row, column)

findPositionOfGuard()

def is_out_of_range(row, column):
    return row >= rowCount or row < 0 or column < 0 or column >= columnCount

def calculateDistinctPositions():
    rowOfGuard, columnOfGuard = findPositionOfGuard()
    visitedDestinations = set()
    currentDirection = up
    continueSearch = True
    visitedDestinations.add((rowOfGuard, columnOfGuard))

    while continueSearch:
            while currentDirection == up:
                rowOfGuard -= 1

                if is_out_of_range(rowOfGuard, columnOfGuard):
                    rowOfGuard += 1
                    continueSearch = False

                    return len(visitedDestinations)
                elif map[rowOfGuard][columnOfGuard] == obstruction:
                    rowOfGuard += 1
                    currentDirection = right

                else:
                    visitedDestinations.add((rowOfGuard, columnOfGuard))

            while currentDirection == right:
                columnOfGuard += 1

                if is_out_of_range(rowOfGuard, columnOfGuard):
                    columnOfGuard -= 1
                    continueSearch = False
                    return len(visitedDestinations)

                elif map[rowOfGuard][columnOfGuard] == obstruction:
                    columnOfGuard -= 1
                    currentDirection = down
                else:
                    visitedDestinations.add((rowOfGuard, columnOfGuard))

            while currentDirection == down:
                rowOfGuard += 1

                if is_out_of_range(rowOfGuard, columnOfGuard):

                    rowOfGuard -= 1
                    continueSearch = False
                    return len(visitedDestinations)

                elif map[rowOfGuard][columnOfGuard] == obstruction:
                    rowOfGuard -= 1
                    currentDirection = left
                else:
                    visitedDestinations.add((rowOfGuard, columnOfGuard))

            while currentDirection == left:
                columnOfGuard -= 1

                if is_out_of_range(rowOfGuard, columnOfGuard):
                    columnOfGuard += 1
                    continueSearch = False
                    return len(visitedDestinations)

                elif map[rowOfGuard][columnOfGuard] == obstruction:
                    columnOfGuard += 1
                    currentDirection = up

                else:
                    visitedDestinations.add((rowOfGuard, columnOfGuard))
                    continueSearch = True

total = calculateDistinctPositions()
print('total', total)
