#!/usr/bin/env python3

from pathlib import Path

def get_priority(item, priority=0):
    if str(item).islower():
        priority = ord(item) - 96  # Convert from ASCII "a"
    elif str(item).isupper():
        priority = ord(item) - 38  # Convert from ASCII "A" minus 27

    return priority

total_priority = 0

p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    for line in file:
        left_compartment = set(line[:len(line)//2])
        right_compartment = set(line[len(line)//2:])

        common_item = set(left_compartment & right_compartment).pop()
        total_priority += get_priority(common_item)
        
print(total_priority)