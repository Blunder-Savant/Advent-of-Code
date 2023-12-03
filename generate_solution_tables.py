from pathlib import Path
from datetime import datetime

HIDDEN_ANCHOR = "<!-- Generate Table Anchor -->\n"

AOC_STARTING_YEAR = 2015
CURRENT_YEAR = datetime.now().year

if __name__ == "__main__":
    # Load current README file
    p = Path(__file__).with_name("README.md")
    with p.open("r", encoding="utf-8") as file:
        readme = file.readlines()

    # Remove everything after the anchor text
    for line_num, line_str in enumerate(readme):
        if line_str == HIDDEN_ANCHOR:
            readme = readme[:line_num + 1]
            break

    # Create a table for each AOC year, if attempted
    for year in range(CURRENT_YEAR, AOC_STARTING_YEAR - 1, -1):
        if (Path.cwd() / str(year)).is_dir():

            readme.append(f"### {year} Results\n")

            # Populate table header
            header = "| | "
            header += " | ".join(f"[Day {day}](https://adventofcode.com/{year}/day/{day})" for day in range(1, 26))
            header += " |\n"
            
            readme.append(header)
            readme.append("| :---: " * 26 + "|\n")

            # Populate part 1 solutions, if available
            part1_results = "| Part 1 | "
            for day in range(1, 26):
                if (Path.cwd() / str(year) / f"Day{str(day).zfill(2)}" / f"{day}A.py").exists():
                    part1_results += f"[⭐]({year}/Day{str(day).zfill(2)}/{day}A.py) | "
                else:
                    part1_results += " | "
            part1_results += "\n"

            readme.append(part1_results)

            # Populate part 2 solutions, if available
            part2_results = "| Part 2 | "
            for day in range(1, 26):
                if (Path.cwd() / str(year) / f"Day{str(day).zfill(2)}" / f"{day}B.py").exists():
                    part2_results += f"[⭐]({year}/Day{str(day).zfill(2)}/{day}B.py) | "
                else:
                    part2_results += " | "
            part2_results += "\n"

            readme.append(part2_results)
            readme.append("\n")

    # Update README file
    p = Path(__file__).with_name("README.md")
    with p.open("w", encoding="utf-8") as file:
        file.writelines(readme)

    print("Executed generate_solution_tables.py")
