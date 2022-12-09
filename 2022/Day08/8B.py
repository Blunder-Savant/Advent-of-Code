#!/usr/bin/env python3

from pathlib import Path

trees = list()

p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    for line in file.read().split():
        trees.append([int(tree) for tree in line]) 

max_scenic_score = 0

for row in range(1, len(trees)-1):
    for col in range(1, len(trees[row])-1): 

        tree_height = trees[row][col]

        left_trees = trees[row][:col]
        right_trees = trees[row][col+1:]
        up_trees = list(zip(*trees))[col][:row]
        down_trees = list(zip(*trees))[col][row+1:]

        scenic_score = 1

        for tree_list in [reversed(left_trees), right_trees, reversed(up_trees), down_trees]:
            for index, tree in enumerate(tree_list):
                if tree >= tree_height:
                    break
            scenic_score *= index + 1

        max_scenic_score = max(max_scenic_score, scenic_score)

print(max_scenic_score)