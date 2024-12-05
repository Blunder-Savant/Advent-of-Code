#!/usr/bin/env python3
from pathlib import Path
import sys

sys.setrecursionlimit(10000)

def beam_travel(x, y, dir):
    if x < 0 or x >= len(layout) or \
       y < 0 or y >= len(layout[0]):
        return

    if ((x, y), dir) in energized:
        return

    piece = layout[x][y]
    energized.add(((x, y), dir))

    if piece == "/":
        if dir == "U": beam_travel(x, y + 1, "R")
        if dir == "D": beam_travel(x, y - 1, "L")
        if dir == "L": beam_travel(x + 1, y, "D")
        if dir == "R": beam_travel(x - 1, y, "U")

    if piece == "\\":
        if dir == "U": beam_travel(x, y - 1, "L")
        if dir == "D": beam_travel(x, y + 1, "R")
        if dir == "L": beam_travel(x - 1, y, "U")
        if dir == "R": beam_travel(x + 1, y, "D")

    if piece == "-":
        if dir in "UD": beam_travel(x, y - 1, "L"), beam_travel(x, y + 1, "R")
        if dir == "L": beam_travel(x, y - 1, "L")
        if dir == "R": beam_travel(x, y + 1, "R")

    if piece == "|":
        if dir in "LR": beam_travel(x - 1, y, "U"), beam_travel(x + 1, y, "D")
        if dir == "U": beam_travel(x - 1, y, "U")
        if dir == "D": beam_travel(x + 1, y, "D")

    if piece == ".":
        if dir == "U": beam_travel(x - 1, y, "U")
        if dir == "D": beam_travel(x + 1, y, "D")
        if dir == "L": beam_travel(x, y - 1, "L")
        if dir == "R": beam_travel(x, y + 1, "R")      


p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    layout = file.read().split()

energized = set()
beam_travel(0, 0, "R")
print(len(set(cell[0] for cell in energized)))
