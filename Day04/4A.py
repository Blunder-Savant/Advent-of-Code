#!/usr/bin/env python3
import re

# Read input from file
with open("puzzle_input.txt") as file:
    input = file.read()

valid_fields = {"byr","iyr","eyr","hgt","hcl","ecl","pid"}
valid_passports = 0

for passport in input.split("\n\n"):
    current_fields = set()

    for field in re.split("[\n, ]", passport):
        key = field[:3]
        
        if key in valid_fields:
            current_fields.add(key)
            
    if current_fields == valid_fields:
        valid_passports += 1

print(valid_passports)