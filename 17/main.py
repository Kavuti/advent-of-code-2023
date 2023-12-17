import math
from pprint import pprint
import os
import heapq


def read_input():
    with open(os.getcwd() + "/input.txt") as f:
        lines = f.read().splitlines()
        return [[int(o) for o in line] for line in lines]


def dijkstra_new_new(lines, min_distance, max_distance):
    q = [(0, 0, 0, -1)]
    adjacents = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = set()
    costs = {}
    while q:
        cost, x, y, cur_dir = heapq.heappop(q)
        if x == len(lines) - 1 and y == len(lines[0]) - 1:
            return cost
        if (x, y, cur_dir) in visited:
            continue
        visited.add((x, y, cur_dir))
        for direction in range(4):
            total_cost = 0
            if direction == cur_dir or (direction + 2) % 4 == cur_dir:
                continue
            for distance in range(1, max_distance + 1):
                new_x = x + adjacents[direction][0] * distance
                new_y = y + adjacents[direction][1] * distance
                if new_x in range(len(lines)) and new_y in range(len(lines[0])):
                    total_cost += lines[new_x][new_y]
                    if distance < min_distance:
                        continue
                    nc = cost + total_cost
                    if costs.get((new_x, new_y, direction), math.inf) <= nc:
                        continue
                    costs[(new_x, new_y, direction)] = nc
                    heapq.heappush(q, (nc, new_x, new_y, direction))


def part1():
    lines = read_input()
    best = dijkstra_new_new(lines, 1, 3)
    print(best)


def part2():
    lines = read_input()
    best = dijkstra_new_new(lines, 4, 10)
    pprint(best)


if __name__ == "__main__":
    part1()
    part2()
