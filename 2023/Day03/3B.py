#!/usr/bin/env python3
from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    schematic = file.read().split("\n")

gear_dict = dict()


def check_engine_for_gear(num_str, row, col):
    for yi in range(row - 1, row + 2):
        for xi in range(col - len(num_str) - 1, col + 1):
            if yi < 0 or yi >= len(schematic) or \
               xi < 0 or xi >= len(schematic[yi]):
                continue

            if schematic[yi][xi] == "*":
                if (yi, xi) not in gear_dict:
                    gear_dict[(yi, xi)] = list()
                gear_dict[(yi, xi)].append(int(num_str))


for yi, line in enumerate(schematic):
    num_str = str()

    for xi, char in enumerate(line):
        if char.isdigit():
            num_str += char
        elif num_str and not char.isdigit():
            check_engine_for_gear(num_str, yi, xi)
            num_str = str()
    if num_str:
        check_engine_for_gear(num_str, yi, xi)

print(sum([nums[0] * nums[1] for nums in gear_dict.values() if len(nums) == 2]))
