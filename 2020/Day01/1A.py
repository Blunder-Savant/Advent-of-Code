#!/usr/bin/env python3

input = set()

# Read input from file
with open("puzzle_input.txt") as file:
    for line in file:
        input.add(int(line))

# Find two numbers that sum to 2020 - O(n)
for num in input:
    diff = 2020 - num
    if diff in input:
        print(num, diff, num*diff)
        break