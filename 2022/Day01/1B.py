#!/usr/bin/env python3

with open("input.txt") as file:
    elf_calories = 0
    elf_calories_list = list()

    for line in file:
        if line == "\n":
            elf_calories_list.append(elf_calories)
            elf_calories = 0
            continue

        meal = int(line)
        elf_calories += meal 

    elf_calories_list.append(elf_calories)

elf_calories_list.sort()
print(sum(elf_calories_list[-3:]))