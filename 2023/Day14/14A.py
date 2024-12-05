#!/usr/bin/env python3
from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    platform = file.read().split("\n")

rolling_rocks = [(x, y) for x, line in enumerate(platform) for y, char in enumerate(line) if char == "O"]
fixed_rocks = [(x, y) for x, line in enumerate(platform) for y, char in enumerate(line) if char == "#"]

new_rolling_rocks = list()

# Tilt platform north
for rock_x, rock_y in rolling_rocks:
    new_x = rock_x
    for x in range(rock_x, 0, -1):
        if (x - 1, rock_y) in new_rolling_rocks or (x - 1, rock_y) in fixed_rocks:
            break
        new_x = x - 1

    new_rolling_rocks.append((new_x, rock_y))

north_load = sum(len(platform) - rock_x for rock_x, _ in new_rolling_rocks)
print(north_load)
