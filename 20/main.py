import os
import copy
import math


def read_input():
    with open(os.getcwd() + "/input.txt") as f:
        lines = f.read().strip().splitlines()
        dicted = {
            l.replace(" ", "")
            .split("->")[0]: l.replace(" ", "")
            .split("->")[1]
            .split(",")
            for l in lines
        }

        dict_keys = list(dicted.keys())
        for key in dict_keys:
            for k, v in dicted.items():
                for i in range(len(v)):
                    if v[i] == key[1:]:
                        v[i] = key
                        break

        return dicted


def negate(signal):
    if signal == "low":
        return "high"
    return "low"


def push_button(modules, state, button_count=1):
    pulses = [("button", "low", "broadcaster")]
    lows, highs = 0, 0
    patterns = {}
    while pulses:
        pulse = pulses.pop(0)
        if pulse[1] == "low":
            lows += 1
        if pulse[1] == "high":
            highs += 1
        if pulse[2] == "broadcaster":
            for module in modules["broadcaster"]:
                pulses.append(("broadcaster", pulse[1], module))
        elif "%" in pulse[2] and pulse[1] == "low":
            current = "high" if pulse[2] in state["on_flip_flops"] else "low"
            for m in modules[pulse[2]]:
                pulses.append((pulse[2], negate(current), m))
            if current == "low":
                state["on_flip_flops"].append(pulse[2])
            else:
                state["on_flip_flops"].remove(pulse[2])
        elif "&" in pulse[2]:
            state["conj_states"][pulse[2]][pulse[0]] = pulse[1]
            to_send = (
                "low"
                if all([s == "high" for k, s in state["conj_states"][pulse[2]].items()])
                else "high"
            )
            if pulse[2][1:] in ["ls", "vc", "nb", "vg"] and to_send == "high":
                patterns[pulse[2][1:]] = patterns.get(pulse[2][1:], 0) + 1
            for module in modules[pulse[2]]:
                pulses.append((pulse[2], to_send, module))
    return state, lows, highs, patterns


def get_initial_state(modules):
    state = {"on_flip_flops": [], "conj_states": {}}
    for m, v in modules.items():
        for d in v:
            if "&" in d:
                state["conj_states"][d] = state["conj_states"].get(d, {})
                state["conj_states"][d][m] = "low"
    return state


def part1():
    modules = read_input()
    initial_state = get_initial_state(modules)
    state = copy.deepcopy(initial_state)
    total_lows, total_highs = 0, 0
    for _ in range(1000):
        state, lows, highs, _ = push_button(modules, state)
        # print(lows, highs)
        total_lows += lows
        total_highs += highs
    print(total_lows * total_highs)


def part2():
    modules = read_input()
    initial_state = get_initial_state(modules)
    state = copy.deepcopy(initial_state)
    dest_modules = [k for k, v in modules.items() if "&lg" in v]
    states_history = []
    for m in dest_modules:
        states_history.append(initial_state["conj_states"][m])
    i = 1
    patts = {}
    for i in range(10000):
        state, _, _, patt = push_button(modules, state, i)
        i += 1
        for k, v in patt.items():
            patts[k] = patts.get(k, [])
            patts[k].append(i)

    print(math.lcm(*[v[0] for k, v in patts.items()]))


if __name__ == "__main__":
    part1()
    part2()
