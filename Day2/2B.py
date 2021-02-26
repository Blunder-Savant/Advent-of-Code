#!/usr/bin/env python3
import re

# Read input from file
with open("puzzle_input.txt") as file:
    input = file.readlines()

correct_passwords = 0

for line in input:
    # Split string with multiple delimiters
    sline = re.split("-| |: ", line)

    char_pos1 = int(sline[0]) - 1
    char_pos2 = int(sline[1]) - 1
    char = sline[2]
    password = sline[3]

    # Determine if password has exactly one matching char position
    if password[char_pos1] == char or password[char_pos2] == char:
        if password[char_pos1] != password[char_pos2]:
            correct_passwords += 1

print(correct_passwords)