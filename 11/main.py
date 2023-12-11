import os


def read_input():
    with open(os.getcwd() + "/input.txt") as f:
        return f.read().splitlines()


def get_galaxies(lines):
    galaxies = []
    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            if char == "#":
                galaxies.append([r, c])
    return galaxies


def get_distance(gal1, gal2):
    return abs(gal1[0] - gal2[0]) + abs(gal1[1] - gal2[1])


def get_expanded_rows_and_cols(lines):
    rows = []
    for i in range(len(lines)):
        if "#" not in lines[i]:
            rows.append(i)

    cols = []
    for i in range(len(lines[0])):
        column = [line[i] for line in lines]
        if "#" not in column:
            cols.append(i)

    return rows, cols


def resolve(multiplier):
    lines = read_input()
    galaxies = get_galaxies(lines)
    exp_rows, exp_cols = get_expanded_rows_and_cols(lines)
    for galaxy in galaxies:
        over_rows = sum([int(galaxy[0] > r) for r in exp_rows])
        over_cols = sum([int(galaxy[1] > c) for c in exp_cols])
        galaxy[0] += over_rows * (multiplier - 1)
        galaxy[1] += over_cols * (multiplier - 1)

    distances = [[0 for _ in galaxies] for _ in galaxies]
    for i, g in enumerate(galaxies):
        for o, g2 in enumerate(galaxies):
            distances[i][o] = get_distance(g, g2)
    return sum([sum(distance) for distance in distances]) // 2


def part1():
    print(resolve(2))


def part2():
    print(resolve(1000000))


if __name__ == "__main__":
    part1()
    part2()
