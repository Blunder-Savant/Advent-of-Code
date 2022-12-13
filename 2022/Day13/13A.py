#!/usr/bin/env python3

from pathlib import Path

def compare_lists(left, right):
    if type(left) is int and type(right) is int:
        return (left > right) - (left < right)

    if type(left) is list and type(right) is list:
        for i in range(min(len(left), len(right))):
            cmp = compare_lists(left[i], right[i])

            if cmp == -1: return -1
            if cmp ==  1: return  1

        return (len(left) > len(right)) - (len(left) < len(right))
 
    if type(left) is int: left = [left]
    if type(right) is int: right = [right]
    return compare_lists(left, right)


p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    lines = [eval(line) for line in file.read().split()]

correct_indices = list()

for i in range(0, len(lines), 2):
    left = lines[i]
    right = lines[i+1]

    if compare_lists(left, right) == -1:
        correct_indices.append(i // 2 + 1)

print(sum(correct_indices))