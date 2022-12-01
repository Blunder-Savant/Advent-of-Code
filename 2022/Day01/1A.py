#!/usr/bin/env python3

from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    groups = file.read().split("\n\n")

elf_calories_max = 0

for group in groups:
    elf_calories = sum([int(meal) for meal in group.split()])
    elf_calories_max = max(elf_calories_max, elf_calories)

print(elf_calories_max)