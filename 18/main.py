import os
import copy
from collections import defaultdict
from pprint import pprint


def read_input():
    with open(os.getcwd() + "/input.txt") as f:
        lines = f.read().splitlines()
        commands = []
        for line in lines:
            s = line.split(" ")
            commands.append((s[0], int(s[1]), s[2][2:-1]))
        return commands


def execute(commands):
    verts = [(0, 0)]
    for c in commands:
        last = verts[-1]
        match c[0]:
            case "R":
                verts.append((last[0], last[1] + c[1]))
            case "D":
                verts.append((last[0] + c[1], last[1]))
            case "L":
                verts.append((last[0], last[1] - c[1]))
            case "U":
                verts.append((last[0] - c[1], last[1]))

    max_x = 0
    min_x = 1000000
    max_y = 0
    min_y = 1000000

    for v in verts:
        max_x = max(max_x, v[0])
        min_x = min(min_x, v[0])
        max_y = max(max_y, v[1])
        min_y = min(min_y, v[1])

    lh = max_x - min_x + 1
    lv = max_y - min_y + 1
    # grid = [["." for _ in range(lv)] for _ in range(lh)]
    # for i in range(len(verts) - 1):
    #     v1 = verts[i]
    #     v2 = verts[i + 1]
    #     if v1[0] == v2[0]:
    #         for o in range(min(v1[1], v2[1]), max(v1[1], v2[1]) + 1):
    #             grid[v1[0]][o] = "#"
    #             # verts.append((v1[0], o))
    #     elif v1[1] == v2[1]:
    #         for o in range(min(v1[0], v2[0]), max(v1[0], v2[0]) + 1):
    #             grid[o][v1[1]] = "#"
    #             # verts.append((o, v1[1]))

    # points = sum([g.count("#") for g in grid])

    points = 0
    for i in range(len(verts) - 1):
        v1 = verts[i]
        v2 = verts[i + 1]
        if v1[0] == v2[0]:
            points += abs(v1[1] - v2[1])
        elif v1[1] == v2[1]:
            points += abs(v1[0] - v2[0])

    total = 0
    for i in range(len(verts) - 1):
        total += (verts[i][1] + verts[i + 1][1]) * (verts[i][0] - verts[i + 1][0])

    total = abs(total)
    total /= 2

    res = total + 1 - (points / 2)
    return int(res + points)


def part1():
    commands = read_input()
    res = execute(commands)
    print(res)


def part2():
    commands = read_input()
    real_commands = []
    for c in commands:
        num = int(c[2][:5], 16)
        dir_num = int(c[2][5])
        dir = ""
        match dir_num:
            case 0:
                dir = "R"
            case 1:
                dir = "D"
            case 2:
                dir = "L"
            case 3:
                dir = "U"
        real_commands.append((dir, num))
    res = execute(real_commands)
    print(res)


if __name__ == "__main__":
    part1()
    part2()
