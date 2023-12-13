import os


def read_input():
    with open(os.getcwd() + "/input.txt") as f:
        data = f.read().splitlines()
        patterns = []
        current_pattern = []
        for line in data:
            if line == "":
                patterns.append(current_pattern)
                current_pattern = []
            else:
                current_pattern.append(line)
        patterns.append(current_pattern)
        return patterns


def check_pattern(pattern, difference=0):
    for i in range(len(pattern) - 1):
        rows_to_check = list(zip(pattern[i::-1], pattern[i + 1 :]))
        wrong = 0
        for r1, r2 in rows_to_check:
            for c1, c2 in zip(r1, r2):
                if c1 != c2:
                    wrong += 1
        if wrong == difference:
            return i

    return -1


def rotate_pattern(matrix):
    rotated = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for o in range(len(matrix[0])):
            rotated[o][len(matrix) - 1 - i] = matrix[i][o]
    return rotated


def part1():
    data = read_input()

    summarized = 0
    for pattern in data:
        rotated = rotate_pattern(pattern)
        vertical = check_pattern(rotated)
        horizontal = check_pattern(pattern)
        summarized += 100 * (horizontal + 1) + vertical + 1

    print(summarized)


def part2():
    data = read_input()
    summarized = 0
    for pattern in data:
        rotated = rotate_pattern(pattern)
        vertical = check_pattern(rotated, difference=1)
        horizontal = check_pattern(pattern, difference=1)
        summarized += 100 * (horizontal + 1) + vertical + 1

    print(summarized)


if __name__ == "__main__":
    part1()
    part2()
