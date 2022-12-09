#!/usr/bin/env python3

from pathlib import Path

trees = list()

p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    for line in file.read().split():
        trees.append([int(tree) for tree in line]) 

visible_trees = len(trees)*2 + len(trees[0])*2 - 4  # Adding edge trees

for row in range(1, len(trees)-1):
    for col in range(1, len(trees[row])-1): 

        tree_height = trees[row][col]

        left_trees = trees[row][:col]
        right_trees = trees[row][col+1:]
        up_trees = list(zip(*trees))[col][:row]
        down_trees = list(zip(*trees))[col][row+1:]

        if any(tree_height > max(tree_list) for tree_list in [left_trees, right_trees, up_trees, down_trees]):
            visible_trees += 1

print(visible_trees)