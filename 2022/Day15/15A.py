#!/usr/bin/env python3

from pathlib import Path

grid = dict()
GIVEN_Y = 2000000

p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    for line in file.readlines():
        sensor_x = int(line.split("=")[1][:-3])
        sensor_y = int(line.split("=")[2][:-24])
        beacon_x = int(line.split("=")[3][:-3])
        beacon_y = int(line.split("=")[4][:-1])

        grid[(sensor_x, sensor_y)] = "S"
        grid[(beacon_x, beacon_y)] = "B"

        manhattan_dist = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)

        y = GIVEN_Y - sensor_y
        x = manhattan_dist - abs(y)

        for x in range(-x + sensor_x, x + sensor_x + 1):
            if (x, GIVEN_Y) not in grid:
                grid[(x, GIVEN_Y)] = "#"

print(len([coord for coord in grid if grid[coord] == "#"]))