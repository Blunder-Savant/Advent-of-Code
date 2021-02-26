#!/usr/bin/env python3

# Read input from file
with open("puzzle_input.txt") as file:
    input = file.readlines()

adapter_ratings = set()

# Store adapters in an ordered list
for adapter in input:
    adapter_ratings.add(int(adapter))

# Add charging outlet and your device's adapters to the list
adapter_ratings.add(0)
adapter_ratings.add(max(adapter_ratings) + 3)


arrangements = 0

def connect_adapters(rating):
    global arrangements

    if max(adapter_ratings) == rating:
        arrangements += 1

    jolt_min = rating + 1
    jolt_max = rating + 3

    potential_ratings = set(range(jolt_min, jolt_max + 1))

    for potential_rating in potential_ratings:
        if potential_rating in adapter_ratings:
            connect_adapters(potential_rating)

connect_adapters(min(adapter_ratings))
print(arrangements)