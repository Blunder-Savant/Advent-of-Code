#!/usr/bin/env python3

from pathlib import Path

cube_sides = {(1,0,0), (0,1,0), (0,0,1), (-1,0,0), (0,-1,0), (0,0,-1)}
cubes = set()
outside_surfaces = 0

def find_exterior_cubes(outside_cubes):
    fringe = [min(outside_cubes)]
    visited = set()

    while fringe:
        cube = fringe.pop(0)

        if cube in visited: 
            continue

        visited.add(cube)

        for side_cube in [(x+cube[0], y+cube[1], z+cube[2]) for x,y,z in cube_sides]:
            if side_cube in outside_cubes:
                fringe.append(side_cube)

    return visited


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

outside_cubes = set()

for x in range(min(x for x,y,z in cubes)-1, max(x for x,y,z in cubes)+2):
    for y in range(min(y for x,y,z in cubes)-1, max(y for x,y,z in cubes)+2):
        for z in range(min(z for x,y,z in cubes)-1, max(z for x,y,z in cubes)+2):
            if (x,y,z) not in cubes:
                outside_cubes.add((x,y,z))

exterior_cubes = find_exterior_cubes(outside_cubes)
interior_cubes = outside_cubes - exterior_cubes

for cube in interior_cubes:
    for side_cube in [(x+cube[0], y+cube[1], z+cube[2]) for x,y,z in cube_sides]:
        if side_cube in cubes:
            outside_surfaces -= 1

print(outside_surfaces)