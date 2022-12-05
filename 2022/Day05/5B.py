#!/usr/bin/env python3

from pathlib import Path

# lol I'm not parsing this from input.txt
stacks = {
    1: "WRF",
    2: "THMCDVWP",
    3: "PMZNL",
    4: "JCHR",
    5: "CPGHQTB",
    6: "GCWLFZ",
    7: "WVLQZJGC",
    8: "PNRFWTVC",
    9: "JWHGRSV"
}

p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    steps = file.readlines()[10:]

    for step in steps:
        num_crates, from_stack, to_stack = [int(x) for x in step.split() if x.isdigit()]

        if num_crates > len(stacks[from_stack]):
            num_crates = len(stacks[from_stack])

        stacks[to_stack] += stacks[from_stack][-num_crates:]
        stacks[from_stack] = stacks[from_stack][:-num_crates]

top_crates = str().join(stack[-1] for stack in stacks.values())
print(top_crates)