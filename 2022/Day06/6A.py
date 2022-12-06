#!/usr/bin/env python3

from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    signal = file.read()

start_marker_size = 4

for index in range(len(signal) - start_marker_size):
    if len(set(signal[index:index+start_marker_size])) == start_marker_size:
        break

print(index + start_marker_size)