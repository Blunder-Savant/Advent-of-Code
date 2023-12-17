#!/usr/bin/env python3
from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    init_sequence = file.read().split(",")

results = list()

for val in init_sequence:
    num = 0
    for char in val:
        num += ord(char)
        num *= 17
        num %= 256

    results.append(num)

print(sum(results))
