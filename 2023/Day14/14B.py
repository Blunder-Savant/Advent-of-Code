#!/usr/bin/env python3
from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    platform = file.read().split("\n")

rolling_rocks = [(x, y) for x, line in enumerate(platform) for y, char in enumerate(line) if char == "O"]
fixed_rocks = [(x, y) for x, line in enumerate(platform) for y, char in enumerate(line) if char == "#"]

DIR = {
    "N": (-1, 0, 0),
    "W": (0, -1, 0),
    "S": (1, 0, len(platform) - 1),
    "E": (0, 1, len(platform[0]) - 1)
}

MAX_CYCLES = 1000000000
cycle_load_tracker = []

while True:
    cycle_load = list()

    # Spin cycle - tilt north, then west, then south, then east
    for dx, dy, size in DIR.values():
        new_rolling_rocks = list()
    
        # Sort rolling rocks, north
        if (dx, dy) == (-1, 0):
            sorted_rolling_rocks = sorted(rolling_rocks, key=lambda coord: coord[0])
        # Sort rolling rocks, west
        if (dx, dy) == (0, -1):
            sorted_rolling_rocks = sorted(rolling_rocks, key=lambda coord: coord[1])
         # Sort rolling rocks, south
        if (dx, dy) == (1, 0):
            sorted_rolling_rocks = sorted(rolling_rocks, key=lambda coord: coord[0], reverse=True)
        # Sort rolling rocks, east
        if (dx, dy) == (0, 1):
            sorted_rolling_rocks = sorted(rolling_rocks, key=lambda coord: coord[1], reverse=True)       
    
        for rock_x, rock_y in sorted_rolling_rocks:
            new_x = rock_x
            new_y = rock_y
    
            if abs(dx) == 1: 
                for x in range(rock_x, size, dx):
                    if (x + dx, rock_y) in new_rolling_rocks or (x + dx, rock_y) in fixed_rocks:
                        break
                    new_x = x + dx
            else:
                for y in range(rock_y, size, dy):
                    if (rock_x, y + dy) in new_rolling_rocks or (rock_x, y + dy) in fixed_rocks:
                        break
                    new_y = y + dy
    
            new_rolling_rocks.append((new_x, new_y))
    
        rolling_rocks = new_rolling_rocks
        cycle_load.append(set(rolling_rocks))

    cycle_load_tracker.append(cycle_load)

    # Break when a cycle is detected
    if cycle_load_tracker.index(cycle_load) != len(cycle_load_tracker) - 1:
        break

cycle_start = cycle_load_tracker.index(cycle_load) + 1
cycle_end = len(cycle_load_tracker)

rolling_rocks = cycle_load_tracker[cycle_start - 1 + ((MAX_CYCLES - cycle_start) % (cycle_end - cycle_start))][-1]
north_load = sum(len(platform) - rock_x for rock_x, _ in rolling_rocks)
print(north_load)
