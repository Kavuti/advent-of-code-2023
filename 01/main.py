import re


def part_1():
    lines = read_file_part1()
    nums = []
    for line in lines:
        line_nums = []
        for num in line:
            if num.isdigit():
                line_nums.append(num)
        number = int(line_nums[0] + line_nums[-1])
        nums.append(number)
    print(sum(nums))


def part_2():
    letters = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    lines = read_file_part2()
    nums = []
    for line in lines:
        first_digit = ""
        last_digit = ""
        line_nums = []
        for i, num in enumerate(line):
            if num.isdigit():
                line_nums.append(num)
            else:
                three = line[i : min(len(line), i + 3)]
                four = line[i : min(len(line), i + 4)]
                five = line[i : min(len(line), i + 5)]
                if three in letters:
                    line_nums.append(letters[three])
                if four in letters:
                    line_nums.append(letters[four])
                if five in letters:
                    line_nums.append(letters[five])
        number = int(line_nums[0] + line_nums[-1])
        nums.append(number)
    print(sum(nums))


def read_file_part1():
    with open("input1.txt", "r") as f:
        return f.read().splitlines()


def read_file_part2():
    with open("input2.txt", "r") as f:
        return f.read().splitlines()


if __name__ == "__main__":
    part_1()
    part_2()
