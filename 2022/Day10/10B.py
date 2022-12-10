#!/usr/bin/env python3

from pathlib import Path

reg_x = 1
cycle = 1

crt = ""
sprite = "#"*3 + "."*37

def update_crt(sprite, cycle):
    global crt
    
    pos = cycle % 40 - 1
    crt += sprite[pos]

    if (cycle % 40) == 0:
        print(crt)
        crt = ""


p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    for line in file:

        update_crt(sprite, cycle)

        if line[0:4] == "noop":
            cycle += 1

        if line[0:4] == "addx":
            val = int(line.split()[1])
            cycle += 1
            update_crt(sprite, cycle)
            cycle += 1
            reg_x += val

        sprite =  "#"*3 + "."*37
        sprite = sprite[-(reg_x-1):] + sprite[:-(reg_x-1)]