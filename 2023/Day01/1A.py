#!/usr/bin/env python3
from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    lines = file.read().split("\n")

cal_value_total = 0

for line in lines:
    digits = str().join(c for c in line if c.isdigit())

    cal_value = int(digits[0] + digits[-1])
    cal_value_total += cal_value

print(cal_value_total)