#!/usr/bin/env python3

# Read input from file
with open("puzzle_input.txt") as file:
    input = file.readlines()

binary_map = {
    66: 49,  # B -> 1
    70: 48,  # F -> 0
    82: 49,  # R -> 1
    76: 48   # L -> 0
}

seat_id_max = 0

for line in input:
    row = int(line[:7].translate(binary_map), 2)
    col = int(line[7:].translate(binary_map), 2)

    seat_id = row * 8 + col

    # Only save highest seat ID
    if seat_id > seat_id_max:
        seat_id_max = seat_id

print(seat_id_max)