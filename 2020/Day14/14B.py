#!/usr/bin/env python3
from itertools import combinations

# Read input from file
with open("puzzle_input.txt") as file:
    input = file.read()

memory = dict()
floating_values = set()

for line in input.split("\n"):
    if line.startswith("mask"):
        # Mask bits to 1
        temp = line[7:]
        temp = temp.replace("X", "0")
        bitmask_ones = int(temp, 2)

        # Mask floating bits to 1
        floating_bits = list()
        temp = line[7:]
        ind = 35
        for bit in temp:
            if bit == "X":
                floating_bits.append(2 ** ind)

            ind -= 1

        s = list(combinations(floating_bits, 3))


    if line.startswith("mem"):
        address, value = line.split(" = ")

        address = int(address.strip("mem[]"))
        value = int(value)

        address |= bitmask_ones

        # Write to all locations with floating bits

# Sum all values in memory
print(sum(memory.values()))
    