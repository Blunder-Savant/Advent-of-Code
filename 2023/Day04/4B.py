#!/usr/bin/env python3
from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    cards = file.read().split("\n")

won_nums = list()
card_instances = dict()

for card in cards:
    card_num, winning_nums, my_nums = card.replace("|", ":").split(":")

    card_num = int(card_num.split(" ")[-1])
    winning_nums = set(int(num) for num in winning_nums.split(" ") if num)
    my_nums = set(int(num) for num in my_nums.split(" ") if num)

    won_nums.append(winning_nums.intersection(my_nums))

    for num in range(card_num, card_num + len(won_nums[-1]) + 1):
        if num not in card_instances:
            card_instances[num] = 0

        if num == card_num:
            card_instances[num] += 1
        else:
            card_instances[num] += card_instances[card_num]

total_scratchcards = sum(card_instances.values())
print(total_scratchcards)
