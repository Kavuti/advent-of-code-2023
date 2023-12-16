from pprint import pprint
import os
import sys

sys.setrecursionlimit(1000000)


def read_input():
    with open(os.getcwd() + "/input.txt") as f:
        return f.read().splitlines()


def move(grid, start_pos, start_dir):
    visited = set()
    cur_pos = start_pos
    cur_dir = start_dir
    to_visit = [(cur_pos, cur_dir)]
    while len(to_visit) > 0:
        cur_pos, cur_dir = to_visit[0]
        to_visit = to_visit[1:]
        if (
            cur_pos[0] > len(grid) - 1
            or cur_pos[0] < 0
            or cur_pos[1] > len(grid[0]) - 1
            or cur_pos[1] < 0
            or (cur_pos, cur_dir) in visited
        ):
            continue
        # print(cur_pos, cur_dir)
        item = grid[cur_pos[0]][cur_pos[1]]
        visited.add((cur_pos, cur_dir))

        if item == "/":
            cur_dir = (-cur_dir[1], -cur_dir[0])
            to_visit.append(
                ((cur_pos[0] + cur_dir[0], cur_pos[1] + cur_dir[1]), cur_dir)
            )
        elif item == "\\":
            cur_dir = (cur_dir[1], cur_dir[0])
            to_visit.append(
                ((cur_pos[0] + cur_dir[0], cur_pos[1] + cur_dir[1]), cur_dir)
            )
        elif item == "|":
            if cur_dir[0] == 0:
                d1 = (-1, 0)
                d2 = (1, 0)
                to_visit.append(
                    (
                        (cur_pos[0] + d1[0], cur_pos[1] + d1[1]),
                        d1,
                    )
                )
                to_visit.append(
                    (
                        (cur_pos[0] + d2[0], cur_pos[1] + d2[1]),
                        d2,
                    )
                )
            else:
                to_visit.append(
                    ((cur_pos[0] + cur_dir[0], cur_pos[1] + cur_dir[1]), cur_dir)
                )
        elif item == "-":
            if cur_dir[1] == 0:
                d1 = (0, -1)
                d2 = (0, 1)
                to_visit.append(
                    (
                        (cur_pos[0] + d1[0], cur_pos[1] + d1[1]),
                        d1,
                    )
                )
                to_visit.append(
                    (
                        (cur_pos[0] + d2[0], cur_pos[1] + d2[1]),
                        d2,
                    )
                )
            else:
                to_visit.append(
                    ((cur_pos[0] + cur_dir[0], cur_pos[1] + cur_dir[1]), cur_dir)
                )
        else:
            to_visit.append(
                ((cur_pos[0] + cur_dir[0], cur_pos[1] + cur_dir[1]), cur_dir)
            )
    return visited


def part1():
    grid = read_input()
    moves = move(grid, (0, 0), (0, 1))
    print(len(set([a[0] for a in moves])))


def part2():
    grid = read_input()
    max_moves = 0
    edges = (
        [((i, 0), (0, 1)) for i in range(len(grid))]
        + [((i, len(grid[0])), (0, -1)) for i in range(len(grid))]
        + [((0, i), (1, 0)) for i in range(len(grid[0]))]
        + [((len(grid), i), (-1, 0)) for i in range(len(grid[0]))]
    )
    for edge, dir in edges:
        moves = move(grid, edge, dir)
        max_moves = max(max_moves, len(set([a[0] for a in moves])))
    print(max_moves)


if __name__ == "__main__":
    part1()
    part2()
