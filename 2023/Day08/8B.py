#!/usr/bin/env python3
from pathlib import Path
import math

p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    documents = file.read().split("\n\n")

inst = documents[0]
node_map = {node[:3]: (node[7:10], node[12:15]) for node in documents[1].split("\n")}

start_nodes = [node for node in node_map.keys() if node[-1] == "A"]
node_steps = list()

for start_node in start_nodes:
    step = 0
    node = start_node

    while node[-1] != "Z":
        dir = inst[step % len(inst)]

        if dir == "L": node = node_map[node][0]
        if dir == "R": node = node_map[node][1]

        step += 1

    node_steps.append(step)

print(math.lcm(*list(node for node in node_steps)))
