def read_input():
    with open("input.txt") as f:
        return f.read().split(",")


def hash(s):
    val = 0
    for char in s:
        asced = ord(char)
        val += asced
        val *= 17
        val %= 256
    return val


def part1():
    strings = read_input()
    sums = 0
    for s in strings:
        h = hash(s.strip())
        sums += h
    print(sums)


def part2():
    strings = read_input()
    boxes = {n: [] for n in range(256)}
    for string in strings:
        if "=" in string:
            equals = string.split("=")
            h = hash(equals[0])
            tupled = (equals[0], int(equals[1]))
            only_labels = [a[0] for a in boxes[h]]
            if equals[0] in only_labels:
                boxes[h][only_labels.index(equals[0])] = tupled
            else:
                boxes[h].append(tupled)
        else:
            minus = string.split("-")
            h = hash(minus[0])
            only_labels = [a[0] for a in boxes[h]]
            if minus[0] in only_labels:
                del boxes[h][only_labels.index(minus[0])]

    power = 0
    for k, v in boxes.items():
        for i, e in enumerate(v):
            power += (int(k) + 1) * (i + 1) * e[1]
    print(power)


if __name__ == "__main__":
    part1()
    part2()
