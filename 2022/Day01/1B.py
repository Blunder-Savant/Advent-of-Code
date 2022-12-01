#!/usr/bin/env python3

from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    groups = file.read().split("\n\n")

elf_calories_list = list()

for group in groups:
    elf_calories = sum([int(meal) for meal in group.split()])
    elf_calories_list.append(elf_calories)

elf_calories_list.sort()

print(sum(elf_calories_list[-3:]))