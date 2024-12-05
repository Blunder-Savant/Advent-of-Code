#!/usr/bin/env python3
from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    init_sequence = file.read().split(",")


def hash(val):
    num = 0
    for char in val:
        num += ord(char)
        num *= 17
        num %= 256

    return num


box_map = dict()

for val in init_sequence:
    if "-" in val:
        label, lens = val.split("-")
        box = hash(label)
        if box in box_map:
            box_map[box].pop(label, 0)

    if "=" in val:
        label, lens = val.split("=")
        box = hash(label)
        if box in box_map:
            box_map[box].update({label: int(lens)})
        else:
            box_map[box] = {label: int(lens)}

print(sum((box + 1) * (i + 1) * lens for box, slots in box_map.items() for i, lens in enumerate(slots.values())))
