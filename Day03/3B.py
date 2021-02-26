#!/usr/bin/env python3

# Read input from file
with open("puzzle_input.txt") as file:
    input = file.readlines()

Xslope = [1,3,5,7,1]
Yslope = [1,1,1,1,2]

Xpos = [0,0,0,0,0]
Ypos = [0,0,0,0,0]
trees = [0,0,0,0,0]

for line in input:
    for trav in range(len(trees)):
        # Loop back to continue tree pattern
        Xpos[trav] %= len(line) - 1
        Ypos[trav] %= Yslope[trav]

        if Ypos[trav] == 0:
            # Check if we hit a tree
            if line[Xpos[trav]] == '#':
                trees[trav] += 1

            # Add toboggan slope
            Xpos[trav] += Xslope[trav]

        Ypos[trav] += 1

product = 1

# Multiply together the number of trees encountered on each of the listed slopes
for trav in trees:
    product *= trav

print(product)