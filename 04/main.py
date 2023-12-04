import re
import os


def read_input():
    with open(os.getcwd() + "/input.txt") as f:
        lines = f.read().splitlines()
        pattern = re.compile(r": (.+)")
        pairs = []
        for line in lines:
            matches = pattern.findall(line)
            numbers = matches[0]
            numbers = numbers.split("|")
            winners = {int(n) for n in numbers[0].strip().split(" ") if n != ""}
            yours = {int(n) for n in numbers[1].strip().split(" ") if n != ""}
            pairs.append((winners, yours))
        return pairs


def part1():
    pairs = read_input()
    points = 0
    for pair in pairs:
        common = pair[0] & pair[1]
        points += 2 ** (len(common) - 1) if len(common) > 0 else 0
    print(points)


def part2():
    pairs = read_input()
    instances = [1 for _ in range(len(pairs))]
    for i, pair in enumerate(pairs):
        common = len(pair[0] & pair[1])
        if common > 0:
            for o in range(i + 1, i + 1 + common):
                if o < len(pairs):
                    instances[o] += instances[i]
    print(sum(instances))


if __name__ == "__main__":
    part1()
    part2()
