#!/usr/bin/env python3

# Read input from file
with open("puzzle_input.txt") as file:
    input = file.readlines()

preamble = 25
prev_numbers = list()

# Load preamble
for line in input[:preamble]:
    prev_numbers.append(int(line))

# Check the rest of numbers
for line in input[preamble:]:
    prev_numbers.append(int(line))
    valid = False
    for num in prev_numbers:
        num2 = int(line) - num

        if num2 in prev_numbers and num != num2:
            valid = True
            break

    if valid == False:
        break

    prev_numbers.pop(0)


invalid_num = int(line)
found_set = False

# Find contiguous set that sums to the invalid number
for ind, line in enumerate(input):

    sum = int(line)
    cont_set = {sum}

    for line2 in input[ind+1:]:
        sum += int(line2)
        cont_set.add(int(line2))

        if sum == invalid_num:
            found_set = True    
            break
        elif sum > invalid_num:
            break

    if found_set == True:
        break

print(min(cont_set) + max(cont_set))

            
