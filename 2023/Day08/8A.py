#!/usr/bin/env python3
from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    documents = file.read().split("\n\n")

inst = documents[0]
node_map = {node[:3]: (node[7:10], node[12:15]) for node in documents[1].split("\n")}

step = 0
node = "AAA"

while node != "ZZZ":
    dir = inst[step % len(inst)]

    if dir == "L": node = node_map[node][0]
    if dir == "R": node = node_map[node][1]

    step += 1

print(step)
