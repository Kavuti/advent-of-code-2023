import os
import math


def read_input():
    with open(os.getcwd() + "/input.txt") as f:
        workflows, parts = f.read().split("\n\n")
        workflows = workflows.strip().splitlines()
        parts = parts.strip().splitlines()
        parts_dicted = []
        for p in parts:
            pd = {}
            p = p[1:-1]
            attrs = p.split(",")
            for attr in attrs:
                attr_split = attr.split("=")
                pd[attr_split[0]] = int(attr_split[1])
            parts_dicted.append(pd)

        workflows_dicted = {}
        for w in workflows:
            name = w[: w.index("{")]
            w = w.replace(name, "")[1:-1]
            rules = w.split(",")
            workflows_dicted[name] = []
            for rule in rules:
                if ":" in rule:
                    rule_split = rule.split(":")
                    workflows_dicted[name].append((rule_split[0], rule_split[1]))
                else:
                    last_rule = workflows_dicted[name][-1]
                    workflows_dicted[name].append(("(not " + last_rule[0] + ")", rule))
        return workflows_dicted, parts_dicted


def get_conditions(workflows, curr):
    conds = []
    previous = ""
    for rule in workflows[curr]:
        if rule[1] in ["A", "R"]:
            conds.append(previous + rule[0] + " and " + rule[1])
            previous += f"(not {rule[0]}) and "
        else:
            subconditions = get_conditions(workflows, rule[1])
            for s in subconditions:
                conds.append(previous + rule[0] + " and " + s)
            previous += f"(not {rule[0]}) and "
    return [c for c in conds if "and A" in c]


def part1():
    workflows, parts = read_input()
    sum_parts = 0
    for p in parts:
        curr_workflow = "in"
        a = p["a"]
        m = p["m"]
        s = p["s"]
        x = p["x"]
        i = 0
        while True:
            rule = workflows[curr_workflow][i]
            if eval(rule[0]):
                if rule[1] == "A":
                    sum_parts += sum([v for v in p.values()])
                    break
                elif rule[1] == "R":
                    break
                else:
                    curr_workflow = rule[1]
                    i = 0
            else:
                i += 1
    print(sum_parts)


def get_conditions_combos(conds):
    total = 0
    for c in conds:
        counters = {key: [1, 4000] for key in "xmas"}
        split = c.split(" and ")
        for r in split:
            if "not" in r:
                r = r[5:-1]
                if r[1] == ">":
                    counters[r[0]][1] = int(r[2:])
                elif r[1] == "<":
                    counters[r[0]][0] = int(r[2:])
            else:
                if r[1] == "<":
                    counters[r[0]][1] = int(r[2:]) - 1
                elif r[1] == ">":
                    counters[r[0]][0] = int(r[2:]) + 1
        total += math.prod(v[1] - v[0] + 1 for v in counters.values())
    return total


def part2():
    workflows, _ = read_input()
    all_conditions = [a.replace(" and A", "") for a in get_conditions(workflows, "in")]
    # Making rules unique
    new_all = []
    for c in all_conditions:
        rules = c.split(" and ")
        res = " and ".join(list(dict.fromkeys(rules)))
        new_all.append(res)

    combs = get_conditions_combos(new_all)
    print(combs)


if __name__ == "__main__":
    part1()
    part2()
