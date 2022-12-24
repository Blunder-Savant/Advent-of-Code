#!/usr/bin/env python3

from pathlib import Path

NORTH, SOUTH, WEST, EAST  = 0, 1, 2, 3

dir_priority = [NORTH, SOUTH, WEST, EAST]
elf_coords = set()
round_count = 0

p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    for y, line in enumerate(file.read().split()):
        for x, scan in enumerate(line):
            if scan == "#":
                elf_coords.add((x,y))

no_elf_moves = 0

while no_elf_moves != len(elf_coords):
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
    no_elf_moves = 0

    for elf_coord, next_elf_coord in next_elf_coords.items():
        if elf_coord == next_elf_coord:
            elf_coords.add(elf_coord)
            no_elf_moves += 1
        elif sum(coord == next_elf_coord for coord in next_elf_coords.values()) == 1:
            elf_coords.add(next_elf_coord)
        else:
            elf_coords.add(elf_coord)

    # Finally, advance direction priority
    dir_priority = dir_priority[1:] + dir_priority[:1]

    round_count += 1


print(round_count)