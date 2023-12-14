import os
from functools import cache


def read_input():
    with open(os.getcwd() + "/input.txt") as f:
        lines = f.read().splitlines()
        grid = []
        for line in lines:
            grid.append(list(line))
        return grid


@cache
def alternative_tilt(grid, direction):
    rotated = []
    if direction == "north":
        rotated = [list(a) for a in list(zip(*grid))]
    if direction == "west":
        rotated = [list(a) for a in list(grid)]
    if direction == "south":
        rotated = [list(a) for a in list(zip(*grid[::-1]))]
    if direction == "east":
        rotated = [list(a[::-1]) for a in grid]
    repeat = True
    while repeat:
        repeat = False
        for row in rotated:
            oos = [i for i, char in enumerate(row) if char == "O"]
            strow = "".join(row)
            for o in oos:
                new_pos = max(
                    [
                        0,
                        strow[:o].rindex("#") + 1 if "#" in strow[:o] else 0,
                        strow[:o].rindex("O") + 1 if "O" in strow[:o] else 0,
                    ]
                )
                if new_pos != o:
                    repeat = True
                    row[o] = "."
                    row[new_pos] = "O"

    if direction == "north":
        return [list(a) for a in list(zip(*rotated))]
    if direction == "west":
        return rotated
    if direction == "south":
        return [list(a) for a in list(zip(*rotated))[::-1]]
    if direction == "east":
        return [a[::-1] for a in rotated]


def to_tuple(grid):
    return tuple([tuple(a) for a in grid])


def get_load(grid):
    mult = len(grid)
    load = 0
    for i in range(len(grid)):
        load += grid[i].count("O") * mult
        mult -= 1
    return load


def sub(l):
    res = []
    for i in range(len(l) - 1):
        res.append(l[i + 1] - l[i])
    return res


def part1():
    grid = read_input()
    tilted = alternative_tilt(to_tuple(grid), "north")
    print(get_load(tilted))


def part2():
    grid = to_tuple(read_input())
    weights = {}
    for i in range(1000):
        grid = to_tuple(alternative_tilt(grid, "north"))
        grid = to_tuple(alternative_tilt(grid, "west"))
        grid = to_tuple(alternative_tilt(grid, "south"))
        grid = to_tuple(alternative_tilt(grid, "east"))

        load = get_load(grid)
        if load not in weights:
            weights[load] = []
        weights[load].append(i + 1)

    # cycle detection
    num = 1000000000
    for k, v in weights.items():
        if len(v) > 1:
            subs = list(set(sub(v)))
            pattern = subs[0]
            second_pattern = []
            if len(subs) > 1:
                second_pattern = subs[1]
            if (num - v[0]) % pattern == 0:
                print(k)
                break
            if second_pattern and (num - v[0]) % second_pattern == 0:
                print(k)
                break

    # print(get_load(grid))


if __name__ == "__main__":
    part1()
    part2()  # 94585
