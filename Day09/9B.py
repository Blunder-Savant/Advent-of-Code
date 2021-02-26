#!/usr/bin/env python3

# Read input from file
with open("puzzle_input.txt") as file:
    input = file.readlines()

preamble = 25
prev_numbers = list()

# Load preamble
for line in input[:preamble]:
    num = int(line)
    prev_numbers.append(num)

# Check the rest of numbers in the message
for line in input[preamble:]:
    num = int(line)
    valid_num = False
    
    # Verify the current number is valid
    for ind, prev_num1 in enumerate(prev_numbers):
        for prev_num2 in prev_numbers[ind+1:]:
            if prev_num1 + prev_num2 == num:
                valid_num = True
                break

    # Exit if invalid number is found
    if valid_num == False:
        break

    # Update queue for next number
    prev_numbers.append(num)
    prev_numbers.pop(0)


invalid_num = num
found_set = False

# Find a contiguous set that sums to the invalid number
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