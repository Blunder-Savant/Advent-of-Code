#!/usr/bin/env python3
from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    cards = file.read().split("\n")


def calculate_score(num):
    if num < 3:
        return num
    return 2 ** (num - 1)


won_nums = list()

for card in cards:
    _, winning_nums, my_nums = card.replace("|", ":").split(":")

    winning_nums = set(int(num) for num in winning_nums.split(" ") if num)
    my_nums = set(int(num) for num in my_nums.split(" ") if num)

    won_nums.append(winning_nums.intersection(my_nums))

total_points = sum(calculate_score(len(won_num)) for won_num in won_nums)
print(total_points)
