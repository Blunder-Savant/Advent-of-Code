#!/usr/bin/env python3

with open("input.txt") as file:
    elf_calories = 0
    elf_calories_max = 0

    for line in file:
        if line == "\n":
            elf_calories_max = max(elf_calories_max, elf_calories)
            elf_calories = 0
            continue

        meal = int(line)
        elf_calories += meal 

    elf_calories_max = max(elf_calories_max, elf_calories)

print(elf_calories_max)