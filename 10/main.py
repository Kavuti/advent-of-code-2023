import os
import sys

sys.setrecursionlimit(1000000)


def read_input():
    with open(os.getcwd() + "/input.txt") as f:
        return f.read().splitlines()


check = {
    "|": [(-1, 1), (0, 0)],
    "-": [(0, 0), (-1, 1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(1, 0), (0, -1)],
    "F": [(1, 0), (0, 1)],
}


def get_start_position(lines):
    for i, line in enumerate(lines):
        try:
            pos = line.index("S")
            return i, pos
        except ValueError:
            pass


def get_path(lines, row, col, path):
    if lines[row][col] == "S":
        if len(path) > 1:
            return path, True
        elif len(path) == 1:
            return path, False
        else:
            new_path = []
            finished = False
            if lines[row - 1][col] in ["|" "7", "F"]:
                new_path, finished = get_path(lines, row - 1, col, path)
                if finished:
                    return new_path, finished
            if lines[row + 1][col] in ["|", "J", "L"]:
                new_path, finished = get_path(lines, row + 1, col, path)
                if finished:
                    return new_path, finished
            if lines[row][col - 1] in ["-", "F", "L"]:
                new_path, finished = get_path(lines, row, col - 1, path)
                if finished:
                    return new_path, finished
            if lines[row][col + 1] in ["-", "J", "7"]:
                new_path, finished = get_path(lines, row, col + 1, path)
                if finished:
                    return new_path, finished
            return path, False
    elif lines[row][col] == ".":
        path.append(row, col)
        return path, False
    else:
        path.append((row, col))
        finished = False
        new_path = []
        if lines[row][col] == "|":
            if (
                lines[row - 1][col] in ["|", "7", "F", "S"]
                and (row - 1, col) not in path
            ):
                new_path, finished = get_path(lines, row - 1, col, path)
                if finished:
                    return new_path, finished
            if (
                lines[row + 1][col] in ["|", "J", "L", "S"]
                and (row + 1, col) not in path
            ):
                new_path, finished = get_path(lines, row + 1, col, path)
                if finished:
                    return new_path, finished
        elif lines[row][col] == "-":
            if (
                lines[row][col - 1] in ["-", "F", "L", "S"]
                and (row, col - 1) not in path
            ):
                new_path, finished = get_path(lines, row, col - 1, path)
                if finished:
                    return new_path, finished
            if (
                lines[row][col + 1] in ["-", "J", "7", "S"]
                and (row, col + 1) not in path
            ):
                new_path, finished = get_path(lines, row, col + 1, path)
                if finished:
                    return new_path, finished
        elif lines[row][col] == "L":
            if (
                lines[row - 1][col] in ["|", "7", "F", "S"]
                and (row - 1, col) not in path
            ):
                new_path, finished = get_path(lines, row - 1, col, path)
                if finished:
                    return new_path, finished
            if (
                lines[row][col + 1] in ["7", "J", "-", "S"]
                and (row, col + 1) not in path
            ):
                new_path, finished = get_path(lines, row, col + 1, path)
                if finished:
                    return new_path, finished
        elif lines[row][col] == "J":
            if (
                lines[row - 1][col] in ["|", "7", "F", "S"]
                and (row - 1, col) not in path
            ):
                new_path, finished = get_path(lines, row - 1, col, path)
                if finished:
                    return new_path, finished
            if (
                lines[row][col - 1] in ["L", "F", "-", "S"]
                and (row, col - 1) not in path
            ):
                new_path, finished = get_path(lines, row, col - 1, path)
                if finished:
                    return new_path, finished
        elif lines[row][col] == "7":
            if (
                lines[row][col - 1] in ["L", "F", "-", "S"]
                and (row, col - 1) not in path
            ):
                new_path, finished = get_path(lines, row, col - 1, path)
                if finished:
                    return new_path, finished
            if (
                lines[row + 1][col] in ["|", "J", "L", "S"]
                and (row + 1, col) not in path
            ):
                new_path, finished = get_path(lines, row + 1, col, path)
                if finished:
                    return new_path, finished
        elif lines[row][col] == "F":
            if (
                lines[row][col + 1] in ["7", "J", "-", "S"]
                and (row, col + 1) not in path
            ):
                new_path, finished = get_path(lines, row, col + 1, path)
                if finished:
                    return new_path, finished
            if (
                lines[row + 1][col] in ["|", "J", "L", "S"]
                and (row + 1, col) not in path
            ):
                new_path, finished = get_path(lines, row + 1, col, path)
                if finished:
                    return new_path, finished
        return new_path, finished


def part1():
    lines = read_input()
    row, col = get_start_position(lines)
    path, finished = get_path(lines, row, col, [])
    if finished:
        distances = [0 for _ in path]
        s = 0
        e = len(distances) - 1
        dist = 1
        while s <= e:
            distances[s] = dist
            distances[e] = dist
            s += 1
            e -= 1
            dist += 1
        print(max(distances))


def find_enclosed(lines, path):
    chars = ["L", "J", "|", "S"]
    others = ["F", "7", "|", "S"]

    enclosed = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if not (i, j) in path:
                firsts = sum([lines[i][: j + 1].count(c) for c in chars])
                seconds = sum([lines[i][: j + 1].count(c) for c in others])
                if firsts % 2 == 1 and seconds % 2 == 1:
                    enclosed += 1
    return enclosed


def part2():
    lines = read_input()
    row, col = get_start_position(lines)
    path, _ = get_path(lines, row, col, [])
    path.append((row, col))
    lines_copy = ["." * len(line) for line in lines]
    for r, c in path:
        lines_copy[r] = lines_copy[r][:c] + lines[r][c] + lines_copy[r][c + 1 :]
    enclosed = find_enclosed(lines_copy, path)
    print(enclosed)


if __name__ == "__main__":
    part1()
    part2()
