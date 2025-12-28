from sympy import *
# ranges are separated by comma
# each range gives its first ID and last ID separated by a dash (-).
# made only of some sequence of digits repeated twice 55 (5 twice), 6464 (64 twice), and 123123 (123 twice) would all be invalid IDs
# leading zeroes = valid

# open, read all lines one at a time
# with open("/Users/melody.shand/Documents/MS/Python/repos/Advent-of-Code-2025/day2_input.txt", "r") as file:
with open("/Users/melody.shand/Documents/MS/Python/repos/Advent-of-Code-2025/day2_input_sample.txt", "r") as file:
    formatted = file.readlines()[0].split(",")

# 11-22 has two invalid IDs, 11 and 22.
# 95-115 has one invalid ID, 99.
# 998-1012 has one invalid ID, 1010.
# 1188511880-1188511890 has one invalid ID, 1188511885.
# 222220-222224 has one invalid ID, 222222.
# 1698522-1698528 contains no invalid IDs.
# 446443-446449 has one invalid ID, 446446.
# 38593856-38593862 has one invalid ID, 38593859.


def find_repeats(formatted_data):
    i = 0
    repeats = 0
    while i < len(formatted_data):
        range = formatted_data[i].split("-")
        start = range[0]
        end = range[1]

        currentId = int(start)

        while currentId <= int(end):
            # loop through each value and determine if %2 == 0
            if is_even(currentId):
                midway = int(len(str(currentId))/2)
                if str(currentId)[0:midway] == str(currentId)[midway:]:
                    repeats = repeats + currentId
            currentId += 1
        i += 1
        # valid = divisible by 101, 1001, 10001, 100001, etc

    return repeats


def is_even(input):
    if len(str(input)) % 2 == 0:
        return True


print("day 2 part 1 answer: ", find_repeats(formatted))

# part 2


# length must be even, cannot be prime

def isprime(number):
    if isprime(number):
        return True


# div by 2,3,3,5
array_test = []

# something wrong here

# 2 digits: 2
# 3 digits: 3
# 4 digits: 4 and 2
# 5 digits: 5
# 6 digits: 6, 3, 2
# 7 digits 7
# 8 digits: 8, 4, 2
# 9 digits: 9, 3
# 10 digits: 10, 5, 2


def find_chonk_size(number):
    if len(number) % 10 == 0:
        return "Divisible by 10, 5, 2"
    elif len(number) % 9 == 0:
        return "Divisible by 9, 3"
    elif len(number) % 8 == 0:
        return "Divisible by 8, 4, 2"
    elif len(number) % 7 == 0:
        return "Divisible by 7"
    elif len(number) % 6 == 0:
        return "Divisible by 6, 3"
    elif len(number) % 5 == 0:
        return "Divisible by 5"
    elif len(number) % 4 == 0:
        return "Divisible by 4, 2"
    elif len(number) % 3 == 0:
        return "Divisible by 3"
    elif len(number) % 2 == 0:
        return "Divisible by 2"


# ****************
def repeats_in_chonks(currentId, chonk_size):
    validIds = []
    for divisor in chonk_size:
        chonk = int(len(str(currentId))/divisor)
        if str(currentId)[0:chonk] == str(currentId)[chonk:]:
            validIds.append(int(currentId))
    return validIds


def incrementValidIds(arrayOfIds):
    sumOfIds = 0
    if not arrayOfIds == None and not len(arrayOfIds) == 0:
        for id in arrayOfIds:
            sumOfIds += id
    return sumOfIds


def find_repeat_chonks(formatted_data):
    i = 0
    part2repeats = 0
    while i < len(formatted_data):
        range = formatted_data[i].split("-")
        start = range[0]
        end = range[1]

        currentId = int(start)

        # loop through each value and determine chonks
        while currentId <= int(end):
            if find_chonk_size(str(currentId)) == "Divisible by 10, 5, 2":
                part2repeats = part2repeats + \
                    incrementValidIds(repeats_in_chonks(currentId, [10, 5, 2]))
            elif find_chonk_size(str(currentId)) == "Divisible by 9, 3":
                part2repeats = part2repeats + \
                    incrementValidIds(repeats_in_chonks(currentId, [9, 3]))
            elif find_chonk_size(str(currentId)) == "Divisible by 8, 4, 2":
                part2repeats = part2repeats + \
                    incrementValidIds(repeats_in_chonks(currentId, [8, 4, 2]))
            elif find_chonk_size(str(currentId)) == "Divisible by 7":
                part2repeats = part2repeats + \
                    incrementValidIds(repeats_in_chonks(currentId, [7]))
            elif find_chonk_size(str(currentId)) == "Divisible by 6, 3":
                part2repeats = part2repeats + \
                    incrementValidIds(repeats_in_chonks(currentId, [6, 3]))
            elif find_chonk_size(str(currentId)) == "Divisible by 5":
                part2repeats = part2repeats + \
                    incrementValidIds(repeats_in_chonks(currentId, [5]))
            elif find_chonk_size(str(currentId)) == "Divisible by 4, 2":
                part2repeats = part2repeats + \
                    incrementValidIds(repeats_in_chonks(currentId, [4, 2]))
            elif find_chonk_size(str(currentId)) == "Divisible by 3":
                part2repeats = part2repeats + \
                    incrementValidIds(repeats_in_chonks(currentId, [3]))
            elif find_chonk_size(str(currentId)) == "Divisible by 2":
                part2repeats = part2repeats + \
                    incrementValidIds(repeats_in_chonks(currentId, [2]))
            currentId += 1
        i += 1
        # valid = divisible by 101, 1001, 10001, 100001, etc

    return part2repeats


print("day 2 part 2 answer: ", find_repeat_chonks(formatted))
