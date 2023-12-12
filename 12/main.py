import os
import sys
from functools import cache

sys.setrecursionlimit(1000000)


def read_input():
    with open(os.getcwd() + "/12/input.txt") as f:
        lines = f.read().splitlines()
        records = []
        for line in lines:
            split = line.split(" ")
            new_record = "".join(split[0])
            records.append((new_record, tuple([int(n) for n in split[1].split(",")])))
        return records


@cache
def count_combos(record, groups):
    print(record, groups)
    if len(record) == 0:
        return 1 if len(groups) == 0 else 0
    if len(groups) == 0:
        return 1 if "#" not in record else 0
    if record[0] == ".":
        return count_combos(record[1:], groups)
    else:
        if record[0] == "#":
            if len(record) < groups[0] or "." in record[: groups[0]]:
                return 0
            elif len(record) == groups[0]:
                return 1 if len(groups) == 1 else 0
            elif len(record) > groups[0]:
                if record[groups[0]] == "#":
                    return 0
                else:
                    return count_combos(record[groups[0] + 1 :], groups[1:])
        return count_combos("#" + record[1:], groups) + count_combos(record[1:], groups)


def unfold(record, groups):
    unfolded = record
    for i in range(4):
        unfolded += "?" + record

    unfolded_groups = groups
    for i in range(4):
        unfolded_groups += groups

    return unfolded, unfolded_groups


def part1():
    records = read_input()
    total = 0
    for record in records:
        # combos = count_combos("".join(record[0]), tuple(record[1]))
        combos = count_combos(*record)
        total += combos
    print(total)


def part2():
    records = read_input()
    total = 0
    for record in records:
        unfolded = unfold(*record)
        total += count_combos(*unfolded)
    print(total)


if __name__ == "__main__":
    part1()
    # part2()
