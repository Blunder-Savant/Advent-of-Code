#!/usr/bin/env python3
from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    surface_pipes = file.read().split("\n")

PIPE_MAP = {
    "|": [(1, 0) , (-1, 0)],
    "-": [(0, 1) , (0, -1)],
    "L": [(-1, 0), (0, 1) ],
    "J": [(-1, 0), (0, -1)],
    "7": [(0, -1), (1, 0) ],
    "F": [(0, 1) , (1, 0) ],
    ".": []
}

# Find starting coordinate
starting_coord = [(x, y) for x, line in enumerate(surface_pipes) for y, char in enumerate(line) if char == "S"][0]

# Find adjacent pipes connected to starting coordinate
starting_next_coords = list()
delta_coords = list()
for x, y in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
    coord = (starting_coord[0] + x, starting_coord[1] + y)

    if coord[0] < 0 or coord[0] >= len(surface_pipes) or \
       coord[1] < 0 or coord[1] >= len(surface_pipes[coord[0]]):
       continue

    pipe = surface_pipes[coord[0]][coord[1]]
    if any(starting_coord == (coord[0] + dx, coord[1] + dy) for dx, dy in PIPE_MAP[pipe]):
        starting_next_coords.append(coord)
        delta_coords.append((x, y))

# Identify and replace starting pipe
starting_pipe = [pipe for pipe in PIPE_MAP if set(delta_coords) == set(PIPE_MAP[pipe])][0]
surface_pipes[starting_coord[0]] = surface_pipes[starting_coord[0]].replace("S", starting_pipe) 

# Generate pipe loop coordinates
coord_path = [starting_coord, starting_next_coords[0]]
while starting_next_coords[1] not in coord_path:
    coord = coord_path[-1]
    pipe = surface_pipes[coord[0]][coord[1]]

    next_coord = [(x, y) for dx, dy in PIPE_MAP[pipe] if (x := coord[0] + dx, y:= coord[1] + dy) not in coord_path][0]
    coord_path.append(next_coord)

# Apply horizontal ray casting to pipe surface. Consider walls as edges in the pipe loop polygon.
# - odd number of walls == inside loop
# - even number of walls == outside loop
inside_pipes = 0 
for x in range(0, len(surface_pipes)):
    wall_count = 0

    for y in range(0, len(surface_pipes[x])):
        if (x, y) in set(coord_path):
            pipe = surface_pipes[x][y]
            if pipe in "|7F":
                wall_count += 1
        else:
            if wall_count % 2 == 1:
                inside_pipes += 1

print(inside_pipes)
