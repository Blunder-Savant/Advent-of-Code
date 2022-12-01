#!/usr/bin/env python3

# Run the program and check if program terminates or has an infinite loop
def check_program(inst_list):
    inst_tracker = set()
    acc = 0
    pc = 0

    while pc not in inst_tracker and pc < len(inst_list):
        inst_tracker.add(pc)

        inst = inst_list[pc]
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

    # Check if program terminates
    if pc == len(inst_list):
        return (True, acc)
    else:
        return (False, None)


# Read input from file
with open("puzzle_input.txt") as file:
    input = file.readlines()

# Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp) 
for ind, inst in enumerate(input):
    op, arg = inst.split()
    new_program = input.copy()

    # Change corrupted instruction
    if op == "acc":
        continue
    elif op == "nop":
        new_program[ind] = new_program[ind].replace(op, "jmp")
    elif op == "jmp":
        new_program[ind] = new_program[ind].replace(op, "nop")

    # Check new program
    finished, acc = check_program(new_program)

    if finished == True: 
        break

print(acc)