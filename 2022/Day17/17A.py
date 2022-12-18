#!/usr/bin/env python3

from pathlib import Path

ROCK_COUNT = 2022
CHAMBER_WIDTH = 7

rock_shapes = {
    0: {(0,0), (1,0), (2,0), (3,0)},         # Row 
    1: {(1,0), (0,1), (1,1), (2,1), (1,2)},  # Plus 
    2: {(0,0), (1,0), (2,0), (2,1), (2,2)},  # Corner
    3: {(0,0), (0,1), (0,2), (0,3)},         # Column
    4: {(0,0), (1,0), (0,1), (1,1)}          # Box
}

stopped_rocks = set((x,0) for x in range(CHAMBER_WIDTH))  # {(x,y)} -- stores coordinates of all stopped rocks


p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    jet_pattern = file.readline().split()[0]
    ji = 0

for ri in range(ROCK_COUNT):
    rock = rock_shapes[ri % len(rock_shapes)]

    rock_x = 2
    rock_y = 4 + max(y for x, y in stopped_rocks)

    while True:
        # Rock either is pushed right or left due to jet of hot gas
        dx = 1 if ">" == jet_pattern[ji % len(jet_pattern)] else -1
        ji += 1

        if all((x + rock_x + dx, y + rock_y) not in stopped_rocks and 0 <= x + rock_x + dx < CHAMBER_WIDTH for x, y in rock):
            rock_x += dx

        # Rock either continues falling or comes to rest
        if all((x + rock_x, y + rock_y - 1) not in stopped_rocks for x, y in rock):
            rock_y -= 1
        else:
            break

    # Store each coordinate of the stopped rock
    stopped_rocks.update({(x + rock_x, y + rock_y) for x, y in rock})

print(max(y for x, y in stopped_rocks))