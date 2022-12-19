#!/usr/bin/env python3

from pathlib import Path
from math import lcm

ROCK_COUNT = 1000000000000
CHAMBER_WIDTH = 7

rock_shapes = {
    0: {(0,0), (1,0), (2,0), (3,0)},         # Row 
    1: {(1,0), (0,1), (1,1), (2,1), (1,2)},  # Plus 
    2: {(0,0), (1,0), (2,0), (2,1), (2,2)},  # Corner
    3: {(0,0), (0,1), (0,2), (0,3)},         # Column
    4: {(0,0), (1,0), (0,1), (1,1)}          # Box
}

# Find how many units tall the tower of rocks
def simulate_rocks_falling(rock_count, jet_pattern):
    stopped_rocks = set((x,0) for x in range(CHAMBER_WIDTH))
    ji = 0
    rock_jet_counts = [ji]

    for ri in range(rock_count):
        rock = rock_shapes[ri % len(rock_shapes)]
    
        rock_x = 2
        rock_y = 4 + max(y for x, y in stopped_rocks)
    
        start_ji = ji
    
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
        rock_jet_counts.append(ji - start_ji)

    return max(y for x, y in stopped_rocks), rock_jet_counts


p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    jet_pattern = file.readline().split()[0]

rocks_base = 1500
# _, rock_jet_counts = simulate_rocks_falling(15000, jet_pattern)

# file = open("Python.txt", "w")  -- LOL manually finding "rocks_base" and "rocks_per_chunk"
# file.write(str(rock_jet_counts))
# file.close()

rocks_per_chunk = 1695

chunk_count = (ROCK_COUNT - rocks_base) // rocks_per_chunk
rocks_top = (ROCK_COUNT - rocks_base) % rocks_per_chunk

base_height = simulate_rocks_falling(rocks_base, jet_pattern)[0]
chunk_height = simulate_rocks_falling(rocks_base + rocks_per_chunk, jet_pattern)[0] - base_height
top_height = simulate_rocks_falling(rocks_base + rocks_top, jet_pattern)[0] - base_height

print(base_height + chunk_height*chunk_count + top_height)