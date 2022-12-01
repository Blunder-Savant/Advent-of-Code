#!/usr/bin/env python3

# Read input from file
with open("puzzle_input.txt") as file:
    input = file.readlines()

adapter_ratings = list()

# Store adapters in an ordered list
for adapter in input:
    adapter_ratings.append(int(adapter))
    adapter_ratings.sort()

# Add charging outlet and your device's adapters to the list
adapter_ratings.insert(0, 0)
adapter_ratings.append(max(adapter_ratings) + 3)

one_jolt_diff = 0
three_jolt_diff = 0

for ind in range(len(adapter_ratings)-1):
    if adapter_ratings[ind+1] - adapter_ratings[ind] == 1:
        one_jolt_diff += 1
    if adapter_ratings[ind+1] - adapter_ratings[ind] == 3:
        three_jolt_diff += 1

print(one_jolt_diff, three_jolt_diff)
print(one_jolt_diff * three_jolt_diff)