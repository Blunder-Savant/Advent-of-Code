#!/usr/bin/env python3

# Read input from file
with open("puzzle_input.txt") as file:
    input = file.read()

ship_direction = 0
ship_x = 0
ship_y = 0

for instruction in input.split("\n"):
    action = instruction[0]
    value = int(instruction[1:])

    if action == "N":
        ship_y += value

    if action == "S":
        ship_y -= value   

    if action == "E":
        ship_x += value

    if action == "W":
        ship_x -= value

    if action == "L":
        ship_direction += value
        ship_direction %= 360

    if action == "R":
        ship_direction -= value
        ship_direction %= 360

    if action == "F":
        if ship_direction == 0:
            ship_x += value

        if ship_direction == 90:
            ship_y += value

        if ship_direction == 180:
            ship_x -= value
            
        if ship_direction == 270:
            ship_y -= value

distance = abs(ship_x) + abs(ship_y)
print(distance)