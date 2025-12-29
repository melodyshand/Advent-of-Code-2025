# with open("/Users/melody.shand/Documents/MS/Python/repos/Advent-of-Code-2025/day3_input_sample.txt", "r") as file:
with open("/Users/melody.shand/Documents/MS/Python/repos/Advent-of-Code-2025/day3_input.txt", "r") as file:
    inputData = file.readlines()
    inputData = [line.strip("\n") for line in inputData]
    inputData = list(inputData)
# each line is a bank
# need to find hhighest 2 digits or digits which give highest number
# find first highest and second highest will only be to the right  of that one


def findHighestFirstNumber(bank):
    maxDigit = max(bank[:-1])
    indexOfMaxDigit = bank.index(maxDigit)
    # cater for this being several
    return {"firstNum": maxDigit, "indexOfMaxDigit": indexOfMaxDigit}


def findHighestSecondNumber(firstNumIndex, bank):
    startOfSlice = firstNumIndex + 1
    maxDigit = max(bank[startOfSlice:])
    indexOfMaxDigit = bank.index(maxDigit)
    # cater for this being several
    return {"secondNum": maxDigit, "indexOfSecondMaxDigit": indexOfMaxDigit}


def formatToJoltage(firstNum, secondNum):
    firstNum = firstNum["firstNum"]
    secondNum = secondNum['secondNum']
    return int(firstNum + secondNum)


def findTotalJoltage():
    joltage = 0

    for bank in inputData:
        firstNumDetails = findHighestFirstNumber(bank)
        firstNumIndex = firstNumDetails["indexOfMaxDigit"]
        secondNumDetails = findHighestSecondNumber(firstNumIndex, bank)
        thisBankJoltage = formatToJoltage(firstNumDetails, secondNumDetails)
        joltage += thisBankJoltage

    print("Day3 part 1 answer: ", joltage)


findTotalJoltage()
