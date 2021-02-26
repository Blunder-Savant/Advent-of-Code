#!/usr/bin/env python3

# Read input from file
with open("puzzle_input.txt") as file:
    input = file.readlines()

pos = 0
trees = 0

for line in input:
    # Loop back to continue tree pattern
    pos %= len(line) - 1

    # Check if we hit a tree
    if line[pos] == '#':
        trees += 1

    # Add toboggan slope
    pos += 3

print(trees)