#!/usr/bin/env python3

# Read input from file
with open("puzzle_input.txt") as file:
    input = file.read()

ship_x = 0
ship_y = 0
waypoint_x = 10
waypoint_y = 1

for instruction in input.split("\n"):
    action = instruction[0]
    value = int(instruction[1:])

    if action == "N":
        waypoint_y += value

    if action == "S":
        waypoint_y -= value    

    if action == "E":
        waypoint_x += value

    if action == "W":
        waypoint_x -= value

    if action == "L":
        if value == 90:
            temp = waypoint_x
            waypoint_x = -1 * waypoint_y
            waypoint_y = temp

        if value == 180:
            waypoint_x = -1 * waypoint_x
            waypoint_y = -1 * waypoint_y

        if value == 270:
            temp = waypoint_x
            waypoint_x = waypoint_y
            waypoint_y = -1 * temp

    if action == "R":
        if value == 90:
            temp = waypoint_x
            waypoint_x = waypoint_y
            waypoint_y = -1 * temp

        if value == 180:
            waypoint_x = -1 * waypoint_x
            waypoint_y = -1 * waypoint_y
            
        if value == 270:
            temp = waypoint_x
            waypoint_x = -1 * waypoint_y
            waypoint_y = temp

    if action == "F":
        ship_x += waypoint_x * value
        ship_y += waypoint_y * value

distance = abs(ship_x) + abs(ship_y)
print(distance)