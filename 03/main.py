import re
import os
from pprint import pprint


def read_input():
    with open(os.getcwd() + "/input.txt", "r") as f:
        return f.read().strip().splitlines()


def contains_symbol(chars):
    return any([(not char.isdigit()) and char != "." for char in chars])


def get_gear_position(chars):
    for i, char in enumerate(chars):
        if char == "*":
            return i
    return -1


def part1():
    grid = read_input()
    pattern = re.compile(r"(\d{1,3})+")
    near = []
    for i, row in enumerate(grid):
        for match in pattern.finditer(row):
            span = match.span()
            near_symbol = False
            start = span[0] - 1 * (span[0] > 0)
            end = span[1] - (1 * (span[1] >= (len(grid[i]) - 1)))

            conditions = [
                i > 0 and contains_symbol(grid[i - 1][start : end + 1]),
                i < len(grid) - 1 and contains_symbol(grid[i + 1][start : end + 1]),
                contains_symbol(grid[i][start]),
                contains_symbol(grid[i][end]),
            ]

            near_symbol = any(conditions)
            if near_symbol:
                near.append(match.group())
    print(sum([int(n) for n in near]))


def part2():
    grid = read_input()
    pattern = re.compile(r"(\d{1,3})+")
    gears = {}
    for i, row in enumerate(grid):
        for match in pattern.finditer(row):
            span = match.span()
            start = span[0] - 1 * (span[0] > 0)
            end = span[1] - (1 * (span[1] >= (len(grid[i]) - 1)))
            positions = [
                get_gear_position(grid[i - 1][start : end + 1]) if i > 0 else -1,
                get_gear_position(grid[i][start : end + 1]),
                get_gear_position(grid[i + 1][start : end + 1])
                if i < len(grid) - 1
                else -1,
            ]

            for o, p in enumerate(positions):
                if p >= 0:
                    tup = (i - 1 + o, span[0] + p - 1)
                    gears[tup] = gears.get(tup, [])
                    gears[tup].append(int(match.group()))
                    break
    valid_gears = [v for v in gears.values() if len(v) >= 2]
    print(sum([v[0] * v[1] for v in valid_gears]))


if __name__ == "__main__":
    part1()
    part2()
