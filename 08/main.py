import math


def read_input():
    with open("input.txt") as f:
        data = f.read().splitlines()
        instructions = data[0]
        nodes = {
            node.split("=")[0].strip(): (
                node.split("=")[1].split(",")[0].strip().replace("(", ""),
                node.split("=")[1].split(",")[1].strip().replace(")", ""),
            )
            for node in data[2 : len(data)]
        }
        return instructions, nodes


def part1():
    instructions, nodes = read_input()
    current_node = "AAA"
    instruction_number = 0
    steps = 0
    while current_node != "ZZZ":
        if instructions[instruction_number] == "L":
            current_node = nodes[current_node][0]
        elif instructions[instruction_number] == "R":
            current_node = nodes[current_node][1]
        instruction_number = (instruction_number + 1) % len(instructions)
        steps += 1
    print(steps)


def get_node_steps(node):
    instructions, nodes = read_input()
    current_node = node
    instruction_number = 0
    steps = 0
    while current_node[-1] != "Z":
        if instructions[instruction_number] == "L":
            current_node = nodes[current_node][0]
        elif instructions[instruction_number] == "R":
            current_node = nodes[current_node][1]
        instruction_number = (instruction_number + 1) % len(instructions)
        steps += 1
    return steps


def part2():
    _, nodes = read_input()
    current_nodes = [node for node in nodes.keys() if node[-1] == "A"]
    current_nodes_steps = [get_node_steps(node) for node in current_nodes]
    print(math.lcm(*current_nodes_steps))


if __name__ == "__main__":
    part1()
    part2()
