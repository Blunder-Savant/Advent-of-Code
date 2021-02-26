#!/usr/bin/env python3
import re

# Read input from file
with open("puzzle_input.txt") as file:
    input = file.read()

valid_fields = {"byr","iyr","eyr","hgt","hcl","ecl","pid"}
valid_passports = 0
eye_colors = {"amb","blu","brn","gry","grn","hzl","oth"}

for passport in input.split("\n\n"):
    current_fields = set()

    for field in re.split("[\n, ]", passport):
        key = field[:3]
        value = field[4:]

        if key == "byr":
            if value.isdecimal():
                birth_year = int(value)
                if birth_year >= 1920 and birth_year <= 2002:
                    current_fields.add(key)

        if key == "iyr":
            if value.isdecimal():
                issue_year = int(value)
                if issue_year >= 2010 and issue_year <= 2020:
                    current_fields.add(key)

        if key == "eyr":
            if value.isdecimal():
                expiration_year = int(value)
                if expiration_year >= 2020 and expiration_year <= 2030:
                    current_fields.add(key)

        if key == "hgt":
            if value.endswith("cm"):
                height = int(value.strip("cm"))
                if height >= 150 and height <= 193:
                    current_fields.add(key)
                    
            if value.endswith("in"):
                height = int(value.strip("in"))
                if height >= 59 and height <= 76:
                    current_fields.add(key)

        if key == "hcl":
            if value[0] == '#':
                try:
                    int(value[1:], 16)
                    current_fields.add(key)
                except ValueError:
                    pass  # value[1:] is not hexadecimal

        if key == "ecl":
            if value in eye_colors:
                current_fields.add(key)

        if key == "pid":
            if value.isdecimal() and len(value) == 9:
                current_fields.add(key)

    if current_fields == valid_fields:
        valid_passports += 1

print(valid_passports)