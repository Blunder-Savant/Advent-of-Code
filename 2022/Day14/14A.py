#!/usr/bin/env python3

from pathlib import Path

cave = dict()
sand_start = (500, 0)

def find_sand_resting_coord(x, y, y_max):
    if y > y_max:
        return -1

    if (x, y+1) not in cave:
        return find_sand_resting_coord(x, y+1, y_max)
    
    if (x-1, y+1) not in cave:
        return find_sand_resting_coord(x-1, y+1, y_max)

    if (x+1, y+1) not in cave:
        return find_sand_resting_coord(x+1, y+1, y_max)

    return (x, y)


p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    for line in file.readlines():
        coords = [tuple(int(i) for i in coord.split(',')) for coord in line.split(" -> ")]

        for i in range(len(coords)-1):
            for j in range(min(coords[i][0], coords[i+1][0]), max(coords[i][0], coords[i+1][0])+1):
                cave[(j, coords[i][1])] = "#"

            for j in range(min(coords[i][1], coords[i+1][1]), max(coords[i][1], coords[i+1][1])+1):
                cave[(coords[i][0], j)] = "#"

y_max = max(y for _, y in cave)

while True:
    sand_coord = find_sand_resting_coord(sand_start[0], sand_start[1], y_max)
    if sand_coord == -1:
        break
    cave[sand_coord] = "o"

print(len([unit for unit in cave.values() if unit == "o"]))