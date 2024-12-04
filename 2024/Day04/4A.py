#!/usr/bin/env python3
from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    puzzle = file.read().split("\n")

ADJ_CHECKS = {
    "U": [(-1,0), (-2,0), (-3,0)],
    "D": [(1,0), (2,0), (3,0)],
    "L": [(0,-1), (0,-2), (0,-3)],
    "R": [(0,1), (0,2), (0,3)],
    "UL": [(-1,-1), (-2,-2), (-3,-3)],
    "UR": [(-1,1), (-2,2), (-3,3)],
    "DL": [(1,-1), (2,-2), (3,-3)],
    "DR": [(1,1), (2,2), (3,3)],
}

xmas_counts = 0

for row in range(len(puzzle)):
    for col in range(len(puzzle[0])):
        # Check for 'X'
        if puzzle[row][col] != 'X':
            continue

        # Check all adjacent directions for 'MAS'
        for dir in ADJ_CHECKS.values():
            try:
                if "MAS" == "".join(puzzle[row+x][col+y] for x,y in dir if row+x >= 0 and col+y >= 0):
                    xmas_counts += 1
            except:
                pass

print(xmas_counts)