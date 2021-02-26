#!/usr/bin/env python3

# Read input from file
with open("puzzle_input.txt") as file:
    input = file.read()

turn = 1
spoken_nums = dict()

# Load starting numbers
for starting_num in input.split(","):
    spoken_nums[int(starting_num)] = list()
    spoken_nums[int(starting_num)].append(turn)
    turn += 1

prev_num = int(starting_num)

while turn <= 2020:
    # Check if first time number is spoken
    if len(spoken_nums[prev_num]) == 1:
        spoken_nums[0].append(turn)
        prev_num = 0

    # Announce how many turns apart the number is from when it was previously spoken
    else:
        diff = spoken_nums[prev_num][-1] - spoken_nums[prev_num][-2]

        if diff not in spoken_nums:
            spoken_nums[diff] = list()

        spoken_nums[diff].append(turn)
        prev_num = diff

    turn += 1

print(prev_num)