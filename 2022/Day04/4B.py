#!/usr/bin/env python3

from pathlib import Path

total_pairs = 0

p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    for line in file:
        first_elf_min, first_elf_max, second_elf_min, second_elf_max = [int(id) for id in line.replace("-", ",").split(",")]

        if first_elf_min >= second_elf_min and second_elf_max >= first_elf_min:
            total_pairs += 1
        elif second_elf_min >= first_elf_min and first_elf_max >= second_elf_min:
            total_pairs += 1

print(total_pairs)