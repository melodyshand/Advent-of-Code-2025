with open("/Users/melody.shand/Documents/MS/Python/repos/Advent-of-Code-2025/day4_input.txt", "r") as file:
    # with open("/Users/melody.shand/Documents/MS/Python/repos/Advent-of-Code-2025/day4_input_sample.txt", "r") as file:
    inputData = [line.split() for line in file]


# NW N NE
#  W @ E
# SW S SE
# NW = line -1, coord -1
# N = line - 1, coord 0
# NE = line -1, coord +1
# W = line 0, coord -1
# E = line 0, coord +1
# SW = line +1, coord -1
# S = line +1, coord 0
# SE = line +1, coord +1


# for each @ symbol we need to find the above corordinates
def isPaperRoll(item):
    if item == "@":
        return True
    else:
        return False


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
     # need to cater to literal edge cases


def findNeighbourItems(currentitemIndex, currentItemLine, inputData, lines, items):
    rolls = 0
    lineIterator = -1
    itemIterator = -1

    while lineIterator < 2:
        itemIterator = -1   # RESET HERE
        while itemIterator < 2:
            if lineIterator == 0 and itemIterator == 0:
                itemIterator += 1
                continue

            elif isOutOfBounds(currentitemIndex, currentItemLine, inputData, lineIterator, itemIterator, lines, items):
                rolls += 0
            elif isPaperRoll(inputData[currentItemLine + lineIterator][0][currentitemIndex + itemIterator]):
                rolls += 1
            itemIterator += 1
        lineIterator += 1

    if rolls < 4:
        return 1
    else:
        return 0

    # coordinates["NW"] = inputData[northLine][currentitemIndex - 1]
    # coordinates["N"] = inputData[northLine][currentitemIndex]
    # coordinates["NE"] = inputData[northLine][currentitemIndex + 1]
    # coordinates["W"] = inputData[currentItemLine][currentitemIndex - 1]
    # coordinates["E"] = inputData[currentItemLine][currentitemIndex + 1]
    # coordinates["SW"] = inputData[southline][currentitemIndex - 1]
    # coordinates["S"] = inputData[southline][currentitemIndex]
    # coordinates["SE"] = inputData[southline][currentitemIndex + 1]


inputData


def findSurroundingRolls(inputData):
    accessibleRolls = 0
    lines = len(inputData)
    items = len(inputData[0][0])
    currentitemLine = 0
    currentItemIndex = 0

    while currentitemLine < lines:
        lineData = list(inputData[currentitemLine])
        currentItemIndex = 0   # RESET HERE
        while currentItemIndex < len(lineData[0]):
            if isPaperRoll(inputData[currentitemLine][0][currentItemIndex]):
                accessibleRolls += findNeighbourItems(
                    currentItemIndex, currentitemLine, inputData, lines, items)
            currentItemIndex += 1
        currentitemLine += 1

    print("Day 4 PART 1 answer: ", accessibleRolls)


findSurroundingRolls(inputData)


# for each line
# for each coordinate
# norths only possible if line not 1
# Wests only possible if coord not 0
# easts only possible if coord not -1
# souths only possible if line not end

# find those values and if they are @ , increment
