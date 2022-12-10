#!/usr/bin/env python3

from pathlib import Path

reg_x = 1
cycle = 1
signal_strength_total = 0

def update_signal_strength(cycle, reg_x):
    global signal_strength_total

    if (cycle % 40) + 20 == 40:
        signal_strength_total += cycle * reg_x


p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    for line in file:

        update_signal_strength(cycle, reg_x)

        if line[0:4] == "noop":
            cycle += 1

        if line[0:4] == "addx":
            val = int(line.split()[1])
            cycle += 1
            update_signal_strength(cycle, reg_x)
            cycle += 1
            reg_x += val
        
print(signal_strength_total)