from pprint import pprint
import os
from functools import cache
from collections import deque
import numpy as np


def read_input():
    with open(os.getcwd() + "/input.txt") as f:
        return f.read().splitlines()


@cache
def mod(n, m):
    return (n + m) % m


def resolve(lines, steps):
    start = (len(lines) // 2, len(lines[0]) // 2, 0)
    for i, l in enumerate(lines):
        if "S" in l:
            start = (i, l.index("S"), 0)
    tiles = deque()
    tiles.append(start)
    visited = set()
    result = set()
    lx = len(lines)
    ly = len(lines[0])
    while tiles:
        tile = tiles.popleft()
        if tile in visited:
            continue
        visited.add(tile)
        x, y, step = tile
        if step == steps:
            result.add(tile)
        else:
            for i, j in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                mod_i = (i + lx) % lx
                mod_j = (j + ly) % ly
                if lines[mod_i][mod_j] != "#":
                    tiles.append((i, j, step + 1))
    return len(result)


start = None


def part1():
    lines = read_input()
    print(resolve(lines, 64))


def part2():
    lines = read_input()
    r1 = 3703  # resolve(lines, len(lines) // 2)
    r2 = 32957  # resolve(lines, len(lines) // 2 + len(lines))
    r3 = 91379  # resolve(lines, len(lines) // 2 + len(lines) * 2)

    eq_system = np.matrix([[0, 0, 1], [1, 1, 1], [4, 2, 1]])
    b = np.array([r1, r2, r3])
    x = np.linalg.solve(eq_system, b).astype(np.int64)
    n = 26501365 // len(lines)

    print(x[0] * n**2 + x[1] * n + x[2])


if __name__ == "__main__":
    part1()
    part2()
