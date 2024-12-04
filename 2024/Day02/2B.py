#!/usr/bin/env python3
from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    reports = file.read().split("\n")

safe_reports = []

for report in reports:
    base_levels = report.split(" ")
    
    for i in range(len(base_levels)):
        levels = base_levels[:i] + base_levels[i+1:]

        if all(1 <= int(l1) - int(l2) <= 3 for l1, l2 in zip(levels, levels[1:])) or \
           all(1 <= int(l2) - int(l1) <= 3 for l1, l2 in zip(levels, levels[1:])):
            safe_reports.append(report)
            break

print(len(safe_reports))