#!/usr/bin/env python3

# Read input from file
with open("puzzle_input.txt") as file:
    input = file.read()

bags_dict = dict()

input = input.replace("bags", "bag")
input = input.replace("contain", "")
input = input.replace("other", "")
input = input.replace(",", "")
input = input.replace(".", "")

# Parse input and extract info to dictionary
for bag in input.split("bag"):
    word = bag.split()

    if len(word) == 0:
        pass

    elif word[0].isdecimal():
        # bag contents (other bags)
        bag = word[1] + word[2]
        bags_dict[key].add(bag)

    elif word[0] == "no":
        # no contents
        pass

    else:
        # bag holder
        key = word[0] + word[1]
        bags_dict[key] = set()


def bag_depth_first_search(search_bag, find_bag):
    bag_found = False

    if find_bag in bags_dict[search_bag]:
        bag_found = True

    else:
        for bag in bags_dict[search_bag]:
            bag_found |= bag_depth_first_search(bag, find_bag)

    return bag_found


count = 0

# Check every bag if it contains a shiny gold bag
for bag in bags_dict:
    if bag_depth_first_search(bag, "shinygold"):
        count += 1

print(count)