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

taken_seats = set()

for line in input:
    row = int(line[:7].translate(binary_map), 2)
    col = int(line[7:].translate(binary_map), 2)

    seat_id = row * 8 + col
    taken_seats.add(seat_id)

# Use set difference to find the only available seat
my_seat = set(range(min(taken_seats), max(taken_seats))) - taken_seats

print(my_seat)