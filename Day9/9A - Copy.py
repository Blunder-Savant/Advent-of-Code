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

print(int(line))