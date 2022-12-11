#!/usr/bin/env python3

from pathlib import Path

class Monkey:
    def __init__(self, num, items, op, test, if_true_monkey, if_false_monkey):
        self.num = num
        self.items = items
        self.op = op
        self.test = test
        self.if_true_monkey = if_true_monkey
        self.if_false_monkey = if_false_monkey
        self.item_inspects = 0

    def apply_op(self, item):
        self.item_inspects += 1
        return eval(self.op.replace("old", str(item)))

monkeys = list()

p = Path(__file__).with_name("input.txt")
with p.open("r") as file:

    for monkey in file.read().split("\n\n"):
        attr_list = monkey.split("\n")

        num = int(attr_list[0][7])
        items = list(int(item) for item in attr_list[1][18:].split(", "))
        op = attr_list[2].split("new = ")[1]
        test = int(attr_list[3].split()[-1])
        if_true_monkey = int(attr_list[4].split()[-1])
        if_false_monkey = int(attr_list[5].split()[-1])

        monkeys.append(Monkey(num, items, op, test, if_true_monkey, if_false_monkey))

for round in range(20):
    for monkey in monkeys:
        for item in monkey.items:
            # Inspect item
            worry_level = monkey.apply_op(item)

            # Relief monkey didn't damage item LOL
            worry_level //= 3

            # Test item and throw it to another monkey
            if worry_level % monkey.test == 0:
                monkeys[monkey.if_true_monkey].items.append(worry_level)
            else:
                monkeys[monkey.if_false_monkey].items.append(worry_level)

        monkey.items.clear()

monkeys.sort(key=lambda monkey: monkey.item_inspects)
print(monkeys[-1].item_inspects * monkeys[-2].item_inspects)