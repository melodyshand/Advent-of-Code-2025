def openFile(pathAmendment):
    parentPath = "/Users/melody.shand/Documents/MS/Python/repos/Advent-of-Code-2025/"
    with open(parentPath + pathAmendment, "r") as file:
        return file.readlines()


def removeNewLines(rawInput):
    item = 0
    while item < len(rawInput):
        if rawInput[item] is not "\n":
            rawInput[item] = rawInput[item].strip("\n")
        item += 1
    return rawInput
