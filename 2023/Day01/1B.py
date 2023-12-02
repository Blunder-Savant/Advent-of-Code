#!/usr/bin/env python3
from pathlib import Path
import string

p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    lines = file.read().split("\n")

valid_digits_map = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
cal_value_total = 0

for line in lines:
    left_digit = None
    right_digit = None

    # Trim left side until a valid digit is found
    while left_digit == None:
        if line[0].isdigit():
            left_digit = line[0]
        elif any(line.startswith(str_digit) for str_digit in valid_digits_map):
            left_digit = str(valid_digits_map[[str_digit for str_digit in valid_digits_map if line.startswith(str_digit)][0]])
        else:
            line = line[1:]

    # Trim right side until a valid digit is found
    while right_digit == None:
        if line[-1].isdigit():
            right_digit = line[-1]
        elif any(line.endswith(str_digit) for str_digit in valid_digits_map):
            right_digit = str(valid_digits_map[[str_digit for str_digit in valid_digits_map if line.endswith(str_digit)][0]])
        else:
            line = line[:-1]

    cal_value_total += int(left_digit + right_digit)

print(cal_value_total)