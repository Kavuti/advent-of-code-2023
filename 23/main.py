from collections import deque, defaultdict
import os
import sys

sys.setrecursionlimit(1000000)


def read_input():
    p = os.getcwd()
    if "/23" not in p:
        p += "/23"
    with open(p + "/input.txt") as f:
        return f.read().splitlines()


def dfs(graph, pos, end, visited=list()):
    count = 1
    visited.append(pos)
    if pos == end:
        return count
    down = 0
    left = 0
    up = 0
    right = 0
    if graph[pos[0]][pos[1]] in ".v":
        if (pos[0] + 1, pos[1]) not in visited and graph[pos[0] + 1][pos[1]] != "#":
            down = dfs(graph, (pos[0] + 1, pos[1]), end, visited.copy())
    if graph[pos[0]][pos[1]] in ".>":
        if (pos[0], pos[1] + 1) not in visited and graph[pos[0]][pos[1] + 1] != "#":
            right = dfs(graph, (pos[0], pos[1] + 1), end, visited.copy())
    if graph[pos[0]][pos[1]] in ".<":
        if (pos[0], pos[1] - 1) not in visited and graph[pos[0]][pos[1] - 1] != "#":
            left = dfs(graph, (pos[0], pos[1] - 1), end, visited.copy())
    if graph[pos[0]][pos[1]] == ".":
        if (pos[0] - 1, pos[1]) not in visited and graph[pos[0] - 1][pos[1]] != "#":
            up = dfs(graph, (pos[0] - 1, pos[1]), end, visited.copy())
    count += max(up, down, left, right)
    return count


def get_near(maze, start):
    nears = []
    for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        new_node = (start[0] + i, start[1] + j)
        if new_node[0] in range(0, len(maze)) and new_node[1] in range(0, len(maze[0])):
            if maze[new_node[0]][new_node[1]] != "#":
                nears.append(new_node)
    return nears


def compress(maze, start, end):
    compressed = defaultdict(dict)
    joints = [start]
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] != "#":
                near = get_near(maze, (i, j))
                if len(near) >= 3 and all(
                    [
                        n[0] in range(len(maze)) and n[1] in range(len(maze[0]))
                        for n in near
                    ]
                ):
                    joints.append((i, j))
    joints.append(end)

    for joint in joints:
        to_visit = deque()
        to_visit.append((joint, [joint]))
        while to_visit:
            current, path = to_visit.popleft()
            nears = get_near(maze, current)
            for near in nears:
                if near in joints and near != path[0]:
                    compressed[path[0]][near] = len(path)
                else:
                    if near not in path:
                        to_visit.append((near, path + [near]))
    return compressed


def bfs(compressed, start, end):
    queue = deque()
    queue.append((start, [start], [0]))
    maximum = 0
    while queue:
        node, path, dist = queue.popleft()
        if node == end:
            maximum = max(maximum, sum(dist))
        else:
            for new_node in compressed[node]:
                if new_node not in path:
                    queue.append(
                        (
                            new_node,
                            path + [new_node],
                            dist + [compressed[node][new_node]],
                        )
                    )

    return maximum


def part1():
    maze = read_input()
    start = maze[0].index(".")
    end = maze[-1].index(".")
    longest = dfs(maze, (0, start), (len(maze) - 1, end)) - 1
    print(longest)


def part2():
    maze = read_input()
    start = maze[0].index(".")
    end = maze[-1].index(".")
    compressed = compress(maze, (0, start), (len(maze) - 1, end))
    longest = bfs(compressed, (0, start), (len(maze) - 1, end))
    print(longest)


if __name__ == "__main__":
    part1()
    part2()
