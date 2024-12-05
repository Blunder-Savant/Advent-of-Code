#!/usr/bin/env python3
from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    memory = file.read()

byte_ptr = 0
multiply_sum = 0

while memory.find("mul(", byte_ptr) != -1:
    # Find next mul instruction
    byte_ptr = memory.find("mul(", byte_ptr) + 4

    # Find its valid right parentheses (max bytes away is two 3 digit nums = 8)
    right = memory.find(")", byte_ptr, byte_ptr + 8)

    # Move on if corrupted
    if right == -1:
        continue

    # Try to extract the two numbers from memory
    try:
        nums = [int(num) for num in memory[byte_ptr:right].split(",")]
        assert len(nums) == 2
    except:
        continue

    # Valid instruction! Multiply the numbers
    multiply_sum += nums[0] * nums[1]

print(multiply_sum)