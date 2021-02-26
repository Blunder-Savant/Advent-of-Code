#!/usr/bin/env python3

# Read input from file
with open("puzzle_input.txt") as file:
    input = file.read()

total_counts = 0

for group in input.split("\n\n"):
    group_count = set(group)

    for person in group.split("\n"):
        group_count.intersection_update(set(person))
    
    total_counts += len(group_count)

print(total_counts)