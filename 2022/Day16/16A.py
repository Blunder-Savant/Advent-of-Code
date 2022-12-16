#!/usr/bin/env python3

from pathlib import Path

flow_rates = dict()  # {valve: flow rate}
next_valves = dict()  # {valve: {next_valve}}
valve_reduced_paths = dict()  # {valve: {next_valve: tunnel_count}} -- reduced to only include valves with a flow rate > 0
max_pressure = 0

START_VALVE = 'AA'
MINUTES_REMAINING = 30


def find_min_tunnels_to_valve(start_valve, end_valve):
    fringe = [(start_valve, 0)]
    visited = set()

    while fringe:
        valve, tunnel_count = fringe.pop(0)

        if valve == end_valve:
            return tunnel_count

        if valve in visited: 
            continue

        visited.add(valve)

        for next_valve in next_valves[valve]:
            fringe.append((next_valve, tunnel_count + 1))


def search(opened, pressure, valve, minutes_left):
    global max_pressure

    if minutes_left <= 0:
        return 

    max_pressure = max(pressure, max_pressure)

    if valve not in opened:
        search(opened.union([valve]), pressure + flow_rates[valve] * minutes_left, valve, minutes_left - 1)
    else:
        for next_valve in [v for v in valve_reduced_paths[valve] if v not in opened]:
            search(opened, pressure, next_valve, minutes_left - valve_reduced_paths[valve][next_valve])


p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    for line in file.readlines():
        valve = line.split()[1]
        rate = int(line.split()[4][5:-1])
        lead_to_valves = set(valve[0:2] for valve in line.split()[9:])

        flow_rates[valve] = rate
        next_valves[valve] = lead_to_valves

for valve in next_valves:
    if flow_rates[valve] > 0 or valve == START_VALVE:
        valve_reduced_paths[valve] = dict()

for v1 in valve_reduced_paths:
    for v2 in valve_reduced_paths:
        if v1 != v2:
            valve_reduced_paths[v1][v2] = find_min_tunnels_to_valve(v1, v2)

search(set([START_VALVE]), 0, START_VALVE, MINUTES_REMAINING-1)

print(max_pressure)