#!/usr/bin/env python3

from pathlib import Path

MAX_MINUTES = 300

start_coord = tuple()
end_coord = tuple()

blizzards = {
    ">": set(),
    "<": set(),
    "^": set(),
    "v": set()
}

walls = {
    "x": list(),
    "y": list()
}

def find_fewest_moves(start_blizzards, start_coord, end_coord):
    minute_count = 0
    fewest_moves = MAX_MINUTES
    blizzards_snapshot = start_blizzards.copy()

    if start_coord[1] == 0:
        # start coord is top-left -- prioritize moving right -> down -> stay -> up -> left
        move_list = [(1,0), (0,1), (0,0), (0,-1), (-1,0)]
    else:
        # start coord is bottom-right -- prioritize moving left -> up -> stay -> down -> right
        move_list = [(-1,0), (0,-1), (0,0), (0,1), (1,0)]

    fringe = [(start_coord, minute_count, start_blizzards)]
    visited = set()

    while fringe:
        my_coord, minute_count, blizzards = fringe.pop()

        if (my_coord, minute_count) in visited:
            continue

        visited.add((my_coord, minute_count))

        if minute_count >= fewest_moves:
            continue

        # Advance blizzards
        blizzards[">"] = {((bx+1) if (bx+1) < walls["x"][1] else 1, by) for bx, by in blizzards[">"]}
        blizzards["v"] = {(bx, (by+1) if (by+1) < walls["y"][1] else 1) for bx, by in blizzards["v"]}
        blizzards["<"] = {((bx-1) if (bx-1) > walls["x"][0] else walls["x"][1]-1, by) for bx, by in blizzards["<"]}
        blizzards["^"] = {(bx, (by-1) if (by-1) > walls["y"][0] else walls["y"][1]-1) for bx, by in blizzards["^"]}

        # Find next moves -- prioritizing direction to end_coord
        for x, y in move_list:
            next_coord = (my_coord[0]+x, (my_coord[1]+y))

            if next_coord == end_coord:
                if minute_count + 1 < fewest_moves:
                    fewest_moves = minute_count + 1 
                    blizzards_snapshot = blizzards.copy()
                break

            if next_coord == start_coord:
                fringe.append((next_coord, minute_count+1, blizzards.copy()))
                continue                

            # Skip if next coord will be intercepted by a blizzard
            if next_coord in blizzards[">"] or next_coord in blizzards["<"] or next_coord in blizzards["^"] or next_coord in blizzards["v"]:
                continue

            # Skip moves going into a wall
            if next_coord[0] <= walls["x"][0] or next_coord[0] >= walls["x"][1] or next_coord[1] <= walls["y"][0] or next_coord[1] >= walls["y"][1]:
                continue

            fringe.append((next_coord, minute_count+1, blizzards.copy()))
    
    return fewest_moves, blizzards_snapshot


p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    for y, line in enumerate(file.read().split()):
        if line.count("#") > 2:
            if y == 0: start_coord = (line.find("."), y)
            if y > 0: end_coord = (line.find("."), y)
        else:
            for x, obj in enumerate(line):
                if obj == ">": blizzards[">"].add((x, y))
                if obj == "<": blizzards["<"].add((x, y))
                if obj == "^": blizzards["^"].add((x, y))
                if obj == "v": blizzards["v"].add((x, y))

    walls["x"].extend([0, len(line)-1])
    walls["y"].extend([0, y])

path1_moves, blizzards = find_fewest_moves(blizzards, start_coord, end_coord)
assert path1_moves < MAX_MINUTES, "MAX_MINUTES too small and didn't find path1."

path2_moves, blizzards = find_fewest_moves(blizzards, end_coord, start_coord)
assert path2_moves < MAX_MINUTES, "MAX_MINUTES too small and didn't find path2."

path3_moves, blizzards = find_fewest_moves(blizzards, start_coord, end_coord)
assert path3_moves < MAX_MINUTES, "MAX_MINUTES too small and didn't find path3."

print(sum([path1_moves, path2_moves, path3_moves]))