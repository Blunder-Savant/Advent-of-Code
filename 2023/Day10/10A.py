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

starting_coord = [(x, y) for x, line in enumerate(surface_pipes) for y, char in enumerate(line) if char == "S"][0]

starting_next_coords = list()
for x, y in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
    coord = (starting_coord[0] + x, starting_coord[1] + y)

    if coord[0] < 0 or coord[0] >= len(surface_pipes) or \
       coord[1] < 0 or coord[1] >= len(surface_pipes[coord[0]]):
       continue

    pipe = surface_pipes[coord[0]][coord[1]]
    if any(starting_coord == (coord[0] + dx, coord[1] + dy) for dx, dy in PIPE_MAP[pipe]):
        starting_next_coords.append(coord)

coord_paths = {
    "0": [starting_coord, starting_next_coords[0]],
    "1": [starting_coord, starting_next_coords[1]]
}

while coord_paths["0"][-1] != coord_paths["1"][-1]:
    for path in coord_paths.keys():
        coord = coord_paths[path][-1]
        pipe = surface_pipes[coord[0]][coord[1]]

        next_pipe = [(x, y) for dx, dy in PIPE_MAP[pipe] if (x := coord[0] + dx, y:= coord[1] + dy) not in coord_paths[path]]
        coord_paths[path].append(next_pipe[0])

print(len(coord_paths["0"]) - 1)
