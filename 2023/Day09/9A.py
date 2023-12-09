#!/usr/bin/env python3
from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    oasis_report = file.read().split("\n")

oasis_report = [[int(num) for num in seq.split()] for seq in oasis_report]
next_values = list()

for seq in oasis_report:
    seq_history = [seq]

    while not all(num == 0 for num in seq_history[-1]):
        new_seq = list(y - x for x, y in zip(seq_history[-1], seq_history[-1][1:]))
        seq_history.append(new_seq)

    num = 0
    for derived_seq in reversed(seq_history[:-1]):
        num = derived_seq[-1] + num

    next_values.append(num)

print(sum(next_values))
