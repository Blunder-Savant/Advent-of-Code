#!/usr/bin/env python3
import re

# Read input from file
with open("puzzle_input.txt") as file:
    input = file.readlines()

correct_passwords = 0

for line in input:
    # Split string with multiple delimiters
    sline = re.split("-| |: ", line)

    min_chars = int(sline[0])
    max_chars = int(sline[1])
    char = sline[2]
    password = sline[3]

    # Count number of char in password
    correct_chars = password.count(char)
    
    # Determine if password is within min and max number of chars
    if correct_chars >= min_chars and correct_chars <= max_chars:
        correct_passwords += 1

print(correct_passwords)