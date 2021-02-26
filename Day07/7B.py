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
        num = int(word[0])
        bag = word[1] + word[2]
        bags_dict[key].add((bag, num))

    elif word[0] == "no":
        # no contents
        pass

    else:
        # bag holder
        key = word[0] + word[1]
        bags_dict[key] = set()


def bag_depth_first_count(search_bag):
    count = 1

    for bag in bags_dict[search_bag]:
        count += bag[1] * bag_depth_first_count(bag[0])

    return count


# Check how many bags are required inside a shiny gold bag
count = bag_depth_first_count("shinygold") - 1

print(count)