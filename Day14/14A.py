#!/usr/bin/env python3

# Read input from file
with open("puzzle_input.txt") as file:
    input = file.read()

memory = dict()

for line in input.split("\n"):
    if line.startswith("mask"):
        # Mask bits to 0
        temp = line[7:]
        temp = temp.replace("X", "1")
        bitmask_zeros = int(temp, 2)

        # Mask bits to 1
        temp = line[7:]
        temp = temp.replace("X", "0")
        bitmask_ones = int(temp, 2)
    
    if line.startswith("mem"):
        address, value = line.split(" = ")

        address = int(address.strip("mem[]"))
        value = int(value)

        value &= bitmask_zeros
        value |= bitmask_ones

        memory[address] = value

# Sum all values in memory
print(sum(memory.values()))
    