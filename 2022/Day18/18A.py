#!/usr/bin/env python3

from pathlib import Path

cube_sides = {(1,0,0), (0,1,0), (0,0,1), (-1,0,0), (0,-1,0), (0,0,-1)}
cubes = set()

outside_surfaces = 0

p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    for line in file.readlines():
        cube = tuple(int(i) for i in line.split(","))
        cubes.add(cube)

        for side_cube in [(x+cube[0], y+cube[1], z+cube[2]) for x,y,z in cube_sides]:
            if side_cube in cubes:
                outside_surfaces -= 1
            else:
                outside_surfaces += 1

print(outside_surfaces)