import os
import math


def read_input():
    with open(os.getcwd() + "/input.txt", "r") as f:
        lines = f.read().splitlines()
        times = [int(n) for n in lines[0].split(":")[1].split(" ") if n != ""]
        distances = [int(n) for n in lines[1].split(":")[1].split(" ") if n != ""]
    return times, distances


def read_input2():
    with open(os.getcwd() + "/input.txt", "r") as f:
        lines = f.read().splitlines()
        times = int(lines[0].split(":")[1].replace(" ", ""))
        distances = int(lines[1].split(":")[1].replace(" ", ""))
    return times, distances


def part1():
    times, distances = read_input()
    winning = [0 for _ in times]
    for race, time in enumerate(times):
        top = math.floor(
            ((time) + math.sqrt(time**2 - 4 * distances[race])) / 2 - 0.1
        )
        bot = math.ceil(((time) - math.sqrt(time**2 - 4 * distances[race])) / 2 + 0.1)
        winning[race] = top - bot + 1
    print(math.prod(winning))


def part2():
    time, distance = read_input2()
    top = math.floor(((time) + math.sqrt(time**2 - 4 * distance)) / 2)
    bot = math.ceil(((time) - math.sqrt(time**2 - 4 * distance)) / 2)

    print(top - bot + 1)


if __name__ == "__main__":
    part1()
    part2()
