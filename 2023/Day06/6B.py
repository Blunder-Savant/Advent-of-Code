#!/usr/bin/env python3
from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    sheet_of_paper = file.read().split("\n")

race_time = int("".join(sheet_of_paper[0].split()[1:]))
race_dist = int("".join(sheet_of_paper[1].split()[1:]))

STARTING_SPEED = 0
valid_new_records = list()

for button_time in range(1, race_time):
    boat_speed = STARTING_SPEED + button_time
    dist_traveled = boat_speed * (race_time - button_time)
    
    if dist_traveled > race_dist:
        valid_new_records.append(button_time)

print(len(valid_new_records))
