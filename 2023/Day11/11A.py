#!/usr/bin/env python3
from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    image = file.read().split("\n")

# Expand galaxy due to "something involving gravitational effects"
empty_rows = [x for x in range(len(image)) if all(image[x][y] == "." for y in range(len(image[0])))]
empty_cols = [y for y in range(len(image[0])) if all(image[x][y] == "." for x in range(len(image)))]

for x in reversed(empty_rows):
    image.insert(x, image[x])

for y in reversed(empty_cols):
    for x in range(len(image)):
        image[x] = image[x][:y] + "." + image[x][y:]

# Generate galaxy pairings
galaxy_coords = {(x, y) for x, line in enumerate(image) for y, char in enumerate(line) if char == "#"}

galaxy_dist_map = set()
for coord in galaxy_coords:
    for other_coord in galaxy_coords:
        if coord != other_coord and (other_coord, coord) not in galaxy_dist_map:
            galaxy_dist_map.add((coord, other_coord))

# Calculate shortest paths
shortest_paths = [abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1]) for coord1, coord2 in galaxy_dist_map]
print(sum(shortest_paths))
