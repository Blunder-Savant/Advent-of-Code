#!/usr/bin/env python3

# Read input from file
with open("puzzle_input.txt") as file:
    input = file.readlines()

inst_tracker = set()
acc = 0
pc = 0

# Check if program terminates or has an infinite loop
while pc not in inst_tracker:
    inst_tracker.add(pc)

    inst = input[pc]
    op, arg = inst.split()

    # Execute instruction
    if op == "acc":
        acc += int(arg)
        pc += 1
    elif op == "nop":
        pc += 1
    elif op == "jmp":
        pc += int(arg)
    else:
        break

print(acc)