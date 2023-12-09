import os


def read_input():
    with open(os.getcwd() + "/input.txt") as f:
        data = f.read().splitlines()
        return [[int(n) for n in line.split(" ")] for line in data]


def resolve_line(line):
    if all([n == 0 for n in line]):
        return [0] + line + [0]
    else:
        contracted = [line[i + 1] - line[i] for i in range(len(line) - 1)]
        below = resolve_line(contracted)
        return [line[0] - below[0]] + line + [line[-1] + below[-1]]


def part1_and_2():
    lines = read_input()
    lasts = []
    firsts = []
    for line in lines:
        resolved = resolve_line(line)
        lasts.append(resolved[-1])
        firsts.append(resolved[0])

    print(sum(lasts))
    print(sum(firsts))


if __name__ == "__main__":
    part1_and_2()
