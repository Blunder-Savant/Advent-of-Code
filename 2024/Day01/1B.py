#!/usr/bin/env python3
from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    lines = file.read().split("\n")

left  = [int(line.split("  ")[0]) for line in lines]
right = [int(line.split("  ")[1]) for line in lines]

similarity_score = sum(v * right.count(v) for v in left)
print(similarity_score)