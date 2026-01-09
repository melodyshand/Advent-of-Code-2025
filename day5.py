# spoiled/fresh
# ingred ids and available ids
# fresh if in any range

import helperFunctions

rawInput = helperFunctions.openFile("day5_input.txt")
# rawInput = helperFunctions.openFile("day5_input_sample.txt")
input = helperFunctions.removeNewLines(rawInput)
x = 1


# Ingredient ID 1 is spoiled because it does not fall into any range.
# Ingredient ID 5 is fresh because it falls into range 3-5.
# Ingredient ID 8 is spoiled.
# Ingredient ID 11 is fresh because it falls into range 10-14.
# Ingredient ID 17 is fresh because it falls into range 16-20 as well as range 12-18.
# Ingredient ID 32 is spoiled.
def separateRangesAndIds(input):
    ranges = []
    ids = []

    separator = input.index("\n")

    for items in input[0:separator]:
        ranges.append(items)

    for items in input[separator + 1:]:
        ids.append(items)

    return (ranges, ids)


def formatRanges(listOfRanges):
    ranges = []
    for rangeString in listOfRanges:
        rangeString = rangeString.split('-')
        individualRange = []
        for rangeIndex in rangeString:
            # individualRange = []
            individualRange.append(int(rangeIndex))
        ranges.append(individualRange)
    return ranges


def formatIds(idStrings):
    ids = []
    for id in idStrings:
        ids.append(int(id))
    return ids


def checkIdInRange(idList, ranges):
    fresh = 0
    freshRanges = []
    for ingredientId in idList:
        for miniRange in ranges:
            rangeStart = miniRange[0]
            rangeEnd = miniRange[1]

            if rangeStart <= ingredientId <= rangeEnd:
                fresh += 1
                freshRanges.append(miniRange)
                break
    return (fresh, freshRanges)


def findAllFreshIds(freshRanges):
    freshIdsFromRanges = []
    for miniRange in freshRanges:
        rangeStart = miniRange[0]
        rangeEnd = miniRange[1] + 1
        number = rangeStart
        while number < rangeEnd:
            if number not in freshIdsFromRanges:
                freshIdsFromRanges.append(number)
            number += 1
# 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, and 20
    numberOfFreshIds = len(freshIdsFromRanges)
    return numberOfFreshIds


def countFreshFromRanges(ranges):
    ranges.sort()
    total = 0

    current_start, current_end = ranges[0]

    for start, end in ranges[1:]:
        if start <= current_end + 1:
            current_end = max(current_end, end)
        else:
            total += current_end - current_start + 1
            current_start, current_end = start, end

    total += current_end - current_start + 1
    return total


def day5Part1(input):
    unformattedRanges, unformattedIds = separateRangesAndIds(input)
    ranges = formatRanges(unformattedRanges)
    ids = formatIds(unformattedIds)
    print("day 5 pt 1 answer: ", checkIdInRange(ids, ranges)[0])
    freshRanges = checkIdInRange(ids, ranges)[1]
    print("day 5 pt 2 answer: ", countFreshFromRanges(ranges))


day5Part1(input)
# check if id is in range
# (['3-5', '10-14', '16-20', '12-18'], ['1', '5', '8', '11', '17', '32'])
