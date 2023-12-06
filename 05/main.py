import re
import os


def read_input():
    combo_map = {}
    with open(os.getcwd() + "/input.txt") as f:
        data = f.read()
        seeds_match = re.search(r"seeds: (.+)", data)
        seeds = [int(seed) for seed in seeds_match.group(1).split(" ")]
        maps_pattern = re.compile(r"(\w+-to-\w+) map:\n((.+\n)+)", re.MULTILINE)
        for map in maps_pattern.finditer(data):
            name = (map.group(1).split("-to-")[0], map.group(1).split("-to-")[1])
            map_lines = map.group(2).split("\n")
            integer_map = [
                [int(n) for n in line.split(" ") if n != ""]
                for line in map_lines
                if line != ""
            ]

            combo_map[name] = integer_map
    return seeds, combo_map


def part1():
    seeds, maps = read_input()
    positions = []
    for seed in seeds:
        current_position = seed
        for map in maps.values():
            for entry in map:
                if (
                    current_position >= entry[1]
                    and current_position < entry[1] + entry[2]
                ):
                    current_position = entry[0] + (current_position - entry[1])
                    break
        positions.append(current_position)
    print(min(positions))


def part2():
    seed_ranges_line, maps = read_input()
    seed_ranges = []
    for i in range(len(seed_ranges_line) // 2):
        seed_ranges.append((seed_ranges_line[i * 2], seed_ranges_line[i * 2 + 1]))

    found = False
    i = 0
    while not found:
        current_position = i
        for map in reversed(maps.values()):
            for entry in map:
                if (
                    current_position >= entry[0]
                    and current_position < entry[0] + entry[2]
                ):
                    current_position = entry[1] + (current_position - entry[0])
                    break
        for seed_range in seed_ranges:
            if current_position >= seed_range[0] and current_position < sum(seed_range):
                found = True
        if not found:
            i += 1

    print(i)


if __name__ == "__main__":
    part1()
    part2()
