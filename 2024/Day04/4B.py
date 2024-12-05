#!/usr/bin/env python3
from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    puzzle = file.read().split("\n")

ADJ_CHECKS = {
    "U": [(-1,-1), (-1,1), (1,-1), (1,1)],
    "D": [(1,-1), (1,1), (-1,-1), (-1,1)],
    "L": [(-1,-1), (1,-1), (1,1), (-1,1)],
    "R": [(1,1), (-1,1), (-1,-1), (1,-1)]
}

xmas_counts = 0

for row in range(len(puzzle)):
    for col in range(len(puzzle[0])):
        # Check for 'A'
        if puzzle[row][col] != 'A':
            continue

        # Check for 'X' pattern using 'MMSS'
        for dir in ADJ_CHECKS.values():
            try:
                if "MMSS" == "".join(puzzle[row+x][col+y] for x,y in dir if row+x >= 0 and col+y >= 0):
                    xmas_counts += 1
            except:
                pass

print(xmas_counts)