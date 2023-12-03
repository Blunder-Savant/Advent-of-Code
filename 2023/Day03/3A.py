#!/usr/bin/env python3
from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    schematic = file.read().split("\n")

part_numbers = list()


def check_part_number(num_str, row, col):
    for yi in range(row - 1, row + 2):
        for xi in range(col - len(num_str) - 1, col + 1):
            if yi < 0 or yi >= len(schematic) or \
               xi < 0 or xi >= len(schematic[yi]):
                continue

            if not schematic[yi][xi].isdigit() and not schematic[yi][xi] == ".":
                return True

    return False


for yi, line in enumerate(schematic):
    num_str = str()

    for xi, char in enumerate(line):
        if char.isdigit():
            num_str += char
        elif num_str and not char.isdigit():
            if check_part_number(num_str, yi, xi):
                part_numbers.append(int(num_str))
            num_str = str()
    if num_str and check_part_number(num_str, yi, xi):
        part_numbers.append(int(num_str))

print(sum(part_numbers))
