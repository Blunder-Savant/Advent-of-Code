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
    group = list()

    for line_num, line in enumerate(file):
        group.append(set(line[:-1]))

        if line_num % 3 == 2:
            common_item = set(group[0] & group[1] & group[2]).pop()
            total_priority += get_priority(common_item)
            group = list()
        
print(total_priority)