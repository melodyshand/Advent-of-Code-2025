# with open("/Users/melody.shand/Documents/MS/Python/repos/Advent-of-Code-2025/day3_input_sample.txt", "r") as file:
with open("/Users/melody.shand/Documents/MS/Python/repos/Advent-of-Code-2025/day3_input.txt", "r") as file:
    # with open("/Users/melody.shand/Documents/MS/Python/repos/Advent-of-Code-2025/day3_input_test.txt", "r") as file:
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

# PART 2
# find the first but has to be less than or equal to-12 away from endf
# for each after we need to check that there are x numbers after from 11 -> 1#


def part2FindHighestFirstNumber(bank):
    maxDigit = max(bank[:-12])
    indexOfMaxDigit = bank.index(maxDigit)
    # cater for this being several
    return {"firstNum": maxDigit, "indexOfMaxDigit": indexOfMaxDigit}


def part2FindTotalJoltage():
    joltage = 0

    for bank in inputData:
        firstNumDetails = part2FindHighestFirstNumber(bank)
        firstNumIndex = firstNumDetails["indexOfMaxDigit"]
        nextNumDetails = part2FindHighestNumber(firstNumIndex, bank)
        thisBankJoltage = formatToJoltage(firstNumDetails, nextNumDetails)
        joltage += thisBankJoltage

    print("Day3 part 2 answer: ", joltage)


def part2FindHighestNumber(firstNumIndex, bank):
    startOfSlice = firstNumIndex + 1
    # check the next highest num in the range of first to -11 to -1

    # need to check the string we are searching in is from start to end
    # but the number of digits remaining after the max = number left between rthat. num and end?
    startOfSlice = firstNumIndex + 1
    nextIndex = -11
    numberInSequence = 2
    values = {}

    while nextIndex <= -1:
        slice_ = bank[startOfSlice:] if nextIndex == - \
            1 else bank[startOfSlice:nextIndex]
        maxDigit = max(slice_)
        indexOfMaxDigit = startOfSlice + slice_.index(maxDigit)

        numberName = str(numberInSequence) + "number"
        numberIndex = str(numberInSequence) + "index"

        values[numberName] = maxDigit
        values[numberIndex] = indexOfMaxDigit

        nextIndex += 1
        numberInSequence += 1
        startOfSlice = indexOfMaxDigit + 1
    return values


def formatToJoltage(firstNum, nextNumDetails):
    firstNum = firstNum["firstNum"]
    numberName = 2
    while numberName <= 12:
        firstNum += nextNumDetails[str(numberName) + "number"]
        numberName += 1
    return int(firstNum)


part2FindTotalJoltage()


def max_joltage_from_bank(bank: str, keep: int = 12) -> int:
    keptDigits = []
    removals_left = len(bank) - keep

    for digit in bank:
        while keptDigits and keptDigits[-1] < digit and removals_left > 0:
            keptDigits.pop()
            removals_left -= 1
        keptDigits.append(digit)

    # If we didn't use all removals, trim from the end
    if removals_left > 0:
        keptDigits = keptDigits[:-removals_left]

    return int("".join(keptDigits))


def part2_find_total_joltage(inputData):
    total = 0

    for bank in inputData:
        total += max_joltage_from_bank(bank)

    print("Day3 part 2 answer:", total)


part2_find_total_joltage(inputData)
