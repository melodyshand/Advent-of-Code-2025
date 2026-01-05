with open("/Users/melody.shand/Documents/MS/Python/repos/Advent-of-Code-2025/day4_input.txt", "r") as file:
    # with open("/Users/melody.shand/Documents/MS/Python/repos/Advent-of-Code-2025/day4_input_sample.txt", "r") as file:
    # inputData = file.readlines().split()
    inputData = [line.strip() for line in file]  # each row is a string

# Directions:
# NW N NE
#  W @ E
# SW S SE

# Check if a cell contains a paper roll


def isPaperRoll(item):
    return item == "@"

# Check if coordinates are out of bounds


def isOutOfBounds(currentitemIndex, currentItemLine, inputData, lineIterator, itemIterator, lines, items):
    if currentItemLine + lineIterator < 0:
        return True
    elif currentItemLine + lineIterator >= lines:
        return True
    elif currentitemIndex + itemIterator < 0:
        return True
    elif currentitemIndex + itemIterator >= items:
        return True
    else:
        return False

# Count neighbouring rolls around a cell


def findNeighbourItems(currentitemIndex, currentItemLine, inputData, lines, items):
    rolls = 0
    lineIterator = -1

    while lineIterator < 2:
        itemIterator = -1
        while itemIterator < 2:
            # skip the center cell
            if lineIterator == 0 and itemIterator == 0:
                itemIterator += 1
                continue

            # skip out-of-bounds positions
            if not isOutOfBounds(currentitemIndex, currentItemLine, inputData, lineIterator, itemIterator, lines, items):
                if isPaperRoll(inputData[currentItemLine + lineIterator][currentitemIndex + itemIterator]):
                    rolls += 1
            itemIterator += 1
        lineIterator += 1

    # accessible if fewer than 4 neighbours
    if rolls < 4:
        return 1
    else:
        return 0

# Count all accessible rolls


def findSurroundingRolls(inputData):
    accessibleRolls = 0
    lines = len(inputData)
    items = len(inputData[0])  # number of columns

    currentitemLine = 0
    while currentitemLine < lines:
        currentItemIndex = 0
        while currentItemIndex < items:
            if isPaperRoll(inputData[currentitemLine][currentItemIndex]):
                accessibleRolls += findNeighbourItems(
                    currentItemIndex, currentitemLine, inputData, lines, items)
            currentItemIndex += 1
        currentitemLine += 1

    print("Day 4 PART 1 answer: ", accessibleRolls)


# Run the calculation
findSurroundingRolls(inputData)


# part 2
# find accessible rows
# remove/replace)?) in 1 go
# repest


def findCoordsAccessibleItems(currentitemIndex, currentItemLine, inputData, lines, items):
    rolls = 0
    lineIterator = -1

    while lineIterator < 2:
        itemIterator = -1

        while itemIterator < 2:
            # skip the center cell
            if lineIterator == 0 and itemIterator == 0:
                itemIterator += 1
                continue

            # skip out-of-bounds positions
            if not isOutOfBounds(currentitemIndex, currentItemLine, inputData, lineIterator, itemIterator, lines, items):
                if isPaperRoll(inputData[currentItemLine + lineIterator][currentitemIndex + itemIterator]):
                    rolls += 1

            itemIterator += 1
        lineIterator += 1

    # accessible if fewer than 4 neighbours
    if rolls < 4:
        return (currentItemLine, currentitemIndex)  # accessible
    else:
        return None


# def numberOfAccessibleRolls(accessibleRolls):
#     numOfRolls = accessibleRolls.keys()
#     return len(numOfRolls)


def removeRolls(inputData, rollsToRemove):
    for (r, c) in rollsToRemove:
        row = list(inputData[r])
        row[c] = '.'
        inputData[r] = ''.join(row)


def countNumberOfRemovals(accessibleRolls):
    return len(accessibleRolls)


def pt2(inputData):
    lines = len(inputData)
    items = len(inputData[0])  # number of columns
    totalRemoved = 0
    currentitemLine = 0

    while True:
        accessibleRolls = []
        currentitemLine = 0

        while currentitemLine < lines:
            currentItemIndex = 0
            while currentItemIndex < items:
                if isPaperRoll(inputData[currentitemLine][currentItemIndex]):
                    coords = findCoordsAccessibleItems(
                        currentItemIndex, currentitemLine, inputData, lines, items)

                    if coords is not None:
                        accessibleRolls.append(coords)

                currentItemIndex += 1
            currentitemLine += 1

        if not accessibleRolls:
            break

        removeRolls(inputData, accessibleRolls)
        totalRemoved += len(accessibleRolls)

    print("Day 4 PART 2 answer: ", totalRemoved)


pt2(inputData)
