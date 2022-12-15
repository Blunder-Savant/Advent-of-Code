#!/usr/bin/env python3

from pathlib import Path

grid = dict()
grid_xrange = dict()

DISTRESS_BEACON_MIN = 0
DISTRESS_BEACON_MAX = 4000000

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

        for y in range(-manhattan_dist + sensor_y, manhattan_dist + sensor_y + 1):
            if y < DISTRESS_BEACON_MIN or y > DISTRESS_BEACON_MAX:
                continue

            x = manhattan_dist - abs(y - sensor_y)

            x_min = -x + sensor_x
            x_max = x + sensor_x

            if x_min < DISTRESS_BEACON_MIN: x_min = DISTRESS_BEACON_MIN
            if x_max > DISTRESS_BEACON_MAX: x_max = DISTRESS_BEACON_MAX

            if y not in grid_xrange:
                grid_xrange[y] = [(x_min, x_max)]
            else:
                grid_xrange[y].append((x_min, x_max))

for y in grid_xrange:
    conseq_max = 0
    for x_min, x_max in sorted(grid_xrange[y]):
        if x_min-1 <= conseq_max <= x_max:
            conseq_max = x_max
            continue
        elif x_max <= conseq_max:
            continue
        
        print((conseq_max + 1) * 4000000 + y)
        break