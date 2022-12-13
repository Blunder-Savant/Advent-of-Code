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

lines.append( [[2]] )
lines.append( [[6]] )
check_swap = True

while check_swap:
    check_swap = False

    for i in range(0, len(lines)-1):
        left = lines[i]
        right = lines[i+1]

        if compare_lists(left, right) == 1:
            lines[i] = right
            lines[i+1] = left
            check_swap = True

decoder_key = [i+1 for i, line in enumerate(lines) if line == [[2]] or line == [[6]]]
print(decoder_key[0] * decoder_key[1])