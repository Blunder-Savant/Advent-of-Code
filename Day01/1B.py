#!/usr/bin/env python3

input = set()

# Read input from file
with open("puzzle_input.txt") as file:
    for line in file:
        input.add(int(line))

# Find three numbers that sum to 2020 - O(n^2)
for num1 in input:
    diff1 = 2020 - num1
    for num2 in input:
        diff2 = diff1 - num2
        if num2 in input and diff2 in input:
            print(num1, num2, diff2, num1*num2*diff2)
            break
