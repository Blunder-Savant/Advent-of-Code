#!/usr/bin/env python3

from pathlib import Path

NORTH, SOUTH, WEST, EAST  = 0, 1, 2, 3
ROUNDS = 10

dir_priority = [NORTH, SOUTH, WEST, EAST]
elf_coords = set()

p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    for y, line in enumerate(file.read().split()):
        for x, scan in enumerate(line):
            if scan == "#":
                elf_coords.add((x,y))

for round in range(ROUNDS):
    next_elf_coords = dict()

    # First half of round -- consider new moves
    for elf_x, elf_y in elf_coords:
        elf_coord = (elf_x, elf_y)

        # Don't move if there are no adjacent elves
        if {(elf_x + x, elf_y + y) for x in range(-1, 2) for y in range(-1, 2) if x != 0 or y != 0}.isdisjoint(elf_coords):
            next_elf_coords[elf_coord] = elf_coord
            continue

        # Propose new move
        for dir in dir_priority:
            if dir == NORTH:
                if {(elf_x-1, elf_y-1), (elf_x, elf_y-1), (elf_x+1, elf_y-1)}.isdisjoint(elf_coords):
                    next_elf_coords[elf_coord] = (elf_x, elf_y-1)
                    break

            if dir == SOUTH:
                if {(elf_x-1, elf_y+1), (elf_x, elf_y+1), (elf_x+1, elf_y+1)}.isdisjoint(elf_coords):
                    next_elf_coords[elf_coord] = (elf_x, elf_y+1)
                    break

            if dir == WEST:
                if {(elf_x-1, elf_y-1), (elf_x-1, elf_y), (elf_x-1, elf_y+1)}.isdisjoint(elf_coords):
                    next_elf_coords[elf_coord] = (elf_x-1, elf_y)
                    break

            if dir == EAST:
                if {(elf_x+1, elf_y-1), (elf_x+1, elf_y), (elf_x+1, elf_y+1)}.isdisjoint(elf_coords):
                    next_elf_coords[elf_coord] = (elf_x+1, elf_y)
                    break

        if elf_coord not in next_elf_coords:
            next_elf_coords[elf_coord] = elf_coord
            
    # Seconds half of round -- simultaneously move elfs!
    elf_coords = set()

    for elf_coord, next_elf_coord in next_elf_coords.items():
        if elf_coord == next_elf_coord:
            elf_coords.add(elf_coord)
        elif sum(coord == next_elf_coord for coord in next_elf_coords.values()) == 1:
            elf_coords.add(next_elf_coord)
        else:
            elf_coords.add(elf_coord)

    # Finally, advance direction priority
    dir_priority = dir_priority[1:] + dir_priority[:1]

# Find empty ground tiles between elves!
x_min = min(x for x,y in elf_coords)
x_max = max(x for x,y in elf_coords)
y_min = min(y for x,y in elf_coords)
y_max = max(y for x,y in elf_coords)

print(len([(x,y) for x in range(x_min, x_max+1) for y in range(y_min, y_max+1) if (x,y) not in elf_coords]))