#!/usr/bin/env python3
from pathlib import Path
import math

p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    sheet_of_paper = file.read().split("\n")

race_times = [int(num) for num in sheet_of_paper[0].split()[1:]]
race_dists = [int(num) for num in sheet_of_paper[1].split()[1:]]
races = list(zip(race_times, race_dists))

STARTING_SPEED = 0
valid_new_records = list()

for race in races:
    valid_new_records.append(list())

    for button_time in range(1, race[0]):
        boat_speed = STARTING_SPEED + button_time
        dist_traveled = boat_speed * (race[0] - button_time)
        
        if dist_traveled > race[1]:
            valid_new_records[-1].append(button_time)

print(math.prod([len(records) for records in valid_new_records]))
