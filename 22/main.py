from collections import defaultdict
import os
import copy
from collections import deque


class Block:
    def __init__(self, stringed, id):
        self.id = id
        left, right = stringed.split("~")
        lt = tuple([int(i) for i in left.split(",")])
        rt = tuple([int(i) for i in right.split(",")])
        self.x = list(range(*sorted([lt[0], rt[0] + 1])))
        self.y = list(range(*sorted([lt[1], rt[1] + 1])))
        self.z = list(range(*sorted([lt[2], rt[2] + 1])))

    def __repr__(self):
        return f"{self.id}:(({self.x[0]}, {self.y[0]}, {self.z[0]}), ({self.x[-1]}, {self.y[-1]}, {self.z[-1]}))"

    def __eq__(self, other):
        return (
            self.id == other.id
            and self.x == other.x
            and self.y == other.y
            and self.z == other.z
        )

    def __hash__(self):
        return hash((self.id, tuple(self.x), tuple(self.y), tuple(self.z)))


def read_input():
    p = os.getcwd()
    if "/22" not in p:
        p += "/22"
    with open(p + "/input.txt") as f:
        lines = f.read().strip().splitlines()
        blocks = tuple([Block(line, i) for i, line in enumerate(lines)])
        return blocks


def do_overlap(lower, upper):
    max_idx = max(len(upper.x), len(upper.y))
    for i in range(max_idx):
        if (
            upper.x[i % len(upper.x)] in lower.x
            and upper.y[i % len(upper.y)] in lower.y
        ):
            return True
    return False


def fall(blocks):
    block_dict = defaultdict(list)
    for b in blocks:
        block_dict[b.z[-1]].append(b)
        if b.z[0] != b.z[-1]:
            block_dict[b.z[0]].append(b)

    for i in range(0, max([b.z[0] for b in blocks]) + 1):
        if i in block_dict:
            new_dict = copy.deepcopy(block_dict)
            for b in block_dict[i]:
                k = i
                met = False
                # target = 0
                while k > 1:
                    for c in block_dict[k - 1]:
                        if do_overlap(c, b):
                            met = True
                    if met:
                        break
                    k -= 1

                if k != i:
                    new_dict[k].append(b)
                    new_dict[i].remove(b)
                    b.z = [z - (i - k) for z in b.z]

            block_dict = new_dict

    return block_dict


def dictify(blocks, fac=-1):
    dicted = defaultdict(list)
    for b in blocks:
        dicted[b.z[fac]].append(b)
    return dicted


def fall_alternative(blocks):
    block_dict = dictify(blocks)
    for i in range(1, max(list(block_dict.keys())) + 1):
        block_dict = dictify(blocks)
        for b in block_dict[i]:
            overlaps = 0
            counter = i
            target = 0
            while counter > 0:
                for c in block_dict[counter - 1]:
                    if do_overlap(b, c):
                        overlaps += 1
                        target = max(target, c.z[-1] + 1)
                if overlaps > 0:
                    break
                counter -= 1
            start = b.z[0]
            for j in range(len(b.z)):
                b.z[j] = target + b.z[j] - start

            pass
    return block_dict


def get_support_dicts(block_dict):
    support_dict = defaultdict(list)
    supported_dict = defaultdict(list)
    for k in list(block_dict.keys()):
        for b in block_dict[k]:
            t = k
            met = False
            while t >= 0 and not met:
                for c in block_dict[t - 1]:
                    if do_overlap(c, b) and c != b:
                        support_dict[c.id].append(b.id)
                        supported_dict[b.id].append(c.id)
                        met = True
                t -= 1
    return support_dict, supported_dict


def compute_remove(blocks, sd, sbd):
    removables = set()
    for b in blocks:
        if b.id in sd:
            cond = True
            for c in sd[b.id]:
                cond = cond and len(set(sbd[c]) - set([b.id])) > 0
            if cond:
                removables.add(b.id)
        else:
            removables.add(b.id)
    return removables


def compute_dropped(blocks, removables, sd, sbd):
    tot = 0
    for b in blocks:
        if b.id in sd and b.id not in removables:
            dropping = set([b.id])
            to_visit = deque()
            to_visit.append(b.id)
            while to_visit:
                curr = to_visit.popleft()
                if curr in sd:
                    for c in sd[curr]:
                        if len(set(sbd[c]) - dropping) == 0:
                            dropping.add(c)
                            if c not in to_visit:
                                to_visit.append(c)
            tot += len(dropping) - 1
    return tot


def part1():
    blocks = read_input()
    block_dict = fall_alternative(blocks)
    sd, sbd = get_support_dicts(block_dict)
    removables = compute_remove(blocks, sd, sbd)
    print(len(removables))
    return removables, sd, sbd


def part2(removables, sd, sbd):
    blocks = read_input()
    dropped = compute_dropped(blocks, removables, sd, sbd)
    print(dropped)


if __name__ == "__main__":
    removables, sd, sbd = part1()
    part2(removables, sd, sbd)
