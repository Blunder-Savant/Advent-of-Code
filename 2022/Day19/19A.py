#!/usr/bin/env python3

from pathlib import Path

WAIT, ORE, CLAY, OBSIDIAN, GEODE = 0, 1, 2, 3, 4
MINUTES_TOTAL = 24

quality_levels = list()

def search_max_geodes(minutes_total, blueprints, max_robots, robots_start, inventory_start):
    fringe = [(minutes_total, robots_start, inventory_start, set())]
    max_geodes_at_time = {minute: 0 for minute in range(minutes_total + 1)}

    while fringe:
        minutes_left, robots, inventory, skipped_last_minute = fringe.pop()

        max_geodes_at_time[minutes_left] = max(max_geodes_at_time[minutes_left], inventory[GEODE])

        if minutes_left <= 0:
            continue

        # Find which robots we can build
        build_robot = [WAIT]
        for resource in blueprints:
            if resource == GEODE or robots[resource] < max_robots[resource]:
                if all(inventory[res] >= blueprints[resource][res] for res in blueprints[resource]):
                    build_robot.append(resource)

        # Always (and only) build a geode robot if we can
        if GEODE in build_robot:
            build_robot = [GEODE]
     
        # Collect from each robot
        for resource in blueprints:
            inventory[resource] += robots[resource]

        # Try building each robot, prioritizing geode -> obsidian -> clay -> ore -> wait (no build).
        # Skip building robot if we chose not to build last iteration.
        for resource in build_robot:
            if resource == WAIT:
                fringe.append((minutes_left-1, robots.copy(), inventory.copy(), set(build_robot)))

            elif resource in skipped_last_minute:
                continue

            else:
                new_robots = robots.copy()
                new_robots[resource] += 1
     
                new_inventory = inventory.copy()
                for res in blueprints[resource]:
                    new_inventory[res] -= blueprints[resource][res]
     
                fringe.append((minutes_left-1, new_robots, new_inventory, set()))

    return max_geodes_at_time[0]


p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    for line in file.readlines():
        blueprint = [int(word) for word in line.split() if word.isdigit()]
        blueprint_id = int(line.split()[1][:-1])

        blueprints = {
            ORE: {ORE: blueprint[0]},
            CLAY: {ORE: blueprint[1]},
            OBSIDIAN: {ORE: blueprint[2], CLAY: blueprint[3]},
            GEODE: {ORE: blueprint[4], OBSIDIAN: blueprint[5]}
        }

        max_robots = {
            ORE: max(blueprints[bp][ORE] for bp in blueprints),
            CLAY: blueprints[OBSIDIAN][CLAY],
            OBSIDIAN: blueprints[GEODE][OBSIDIAN]
        }

        robots = {ORE: 1, CLAY: 0, OBSIDIAN: 0, GEODE: 0}
        inventory = {ORE: 0, CLAY: 0, OBSIDIAN: 0, GEODE: 0}

        geode_count = search_max_geodes(MINUTES_TOTAL, blueprints, max_robots, robots, inventory)
        quality_levels.append(blueprint_id * geode_count)
    
print(sum(quality_levels))