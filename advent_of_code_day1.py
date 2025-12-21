f = open("adventOfCode/Day1.txt")
data = f.read()
# print(data)
data = data.split("\n")
# data = ['L123', 'L10', 'L24', 'R17']

num_of_zeros = 0
calc_current_position = 0
array_of_nums = []


# numbers run from 0 to 99
# L is decreasing
# R is increasing
# starting position is 50
#for each of the positions we need to determine firstly if it is L or R
# then need to determine the number - need current position, and if the number is decreasing and is greater than the current number, go back down to counting down from 99
# determine by how much the current position is shifting, either as a positive or negative number
def dec_or_inc(x):
        if x[0] == "L":
            number = int(x.split("L")[1])
            output = -number
            # print(x)
            return (output)

        elif x[0] == "R":
            number = int(x.split("R")[1])
            output = number
            return (output)

#take current position and the inc/dec to find new position
def find_new_number(number, current_position): 
    # the incrementer/decrementer can be bigger than 100, either positive or negative, so need to find what is left once modded past 100
    times_passed_zero = number % 100
    
    if number > 0:
        new_current_position = current_position + times_passed_zero
    
    if number < 0:
        new_current_position = (current_position + times_passed_zero) - 100
    return new_current_position
   

def find_all_nums(input):
    i = 0

    #loop through the array of L and R numbers and for each determine by how uch we are shifting the current position by
    #new number then finds the next position by taking in the number to shift by and the current position
    #array_of_nums is the position, used
    #calc_current position is an array of the current position, meant to be used int he case of i > 0
    while i < len(input):
        if i == 0:
            current_position = 50
            input_number =  dec_or_inc(input[i])
            new_number = find_new_number(input_number, current_position)
            array_of_nums.append(new_number)
            i = i + 1   
        else:
            #number to be added on to current position
            input_number =  dec_or_inc(input[i])
            new_number = find_new_number(input_number, array_of_nums[i-1])
            array_of_nums.append(new_number)
            i = i + 1

    return array_of_nums

def find_zeroes(input_array):
    num_of_zeros = 0
    for i in input_array:
        if i == 0:
            num_of_zeros = num_of_zeros + 1
    return num_of_zeros


array_to_search = find_all_nums(data)
print(find_zeroes(array_to_search))

