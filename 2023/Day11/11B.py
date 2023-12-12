#!/usr/bin/env python3
from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    image = file.read().split("\n")

EXPANSION_RATE = 1000000

# Find galaxy expansion rows and cols due to "something involving gravitational effects"
empty_rows = [x for x in range(len(image)) if all(image[x][y] == "." for y in range(len(image[0])))]
empty_cols = [y for y in range(len(image[0])) if all(image[x][y] == "." for x in range(len(image)))]

# Generate galaxy pairings
galaxy_coords = {(x, y) for x, line in enumerate(image) for y, char in enumerate(line) if char == "#"}

galaxy_dist_map = set()
for coord in galaxy_coords:
    for other_coord in galaxy_coords:
        if coord != other_coord and (other_coord, coord) not in galaxy_dist_map:
            galaxy_dist_map.add((coord, other_coord))

# Calculate shortest paths
shortest_paths = list()
for coord1, coord2 in galaxy_dist_map:
    max_x, min_x = max(coord1[0], coord2[0]), min(coord1[0], coord2[0])
    max_y, min_y = max(coord1[1], coord2[1]), min(coord1[1], coord2[1])

    expansion_x = len([empty_x for empty_x in empty_rows if max_x > empty_x > min_x]) * (EXPANSION_RATE - 1)
    expansion_y = len([empty_y for empty_y in empty_cols if max_y > empty_y > min_y]) * (EXPANSION_RATE - 1)

    dist = (max_x - min_x) + expansion_x + (max_y - min_y) + expansion_y
    shortest_paths.append(dist)

print(sum(shortest_paths))
