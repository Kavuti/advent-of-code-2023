from collections import deque, defaultdict
import copy
import os

import matplotlib.pyplot as plt
import networkx as nx


def read_input():
    p = os.getcwd()
    if "/25" not in p:
        p += "/25"
    with open(p + "/input.txt", "r") as f:
        lines = f.read().splitlines()
        edges = []
        for line in lines:
            split = line.split(":")
            first = split[0].strip()
            others = split[1].strip().split(" ")
            for o in others:
                edges.append((first, o))
        return edges


def bfs(data, start=None, end=None):
    visited = set()
    to_visit = deque()
    if start:
        to_visit.append(start)
    else:
        to_visit.append(list(data.keys())[0])
    while to_visit:
        curr = to_visit.popleft()
        if curr in visited:
            continue
        visited.add(curr)
        if end and curr == end:
            break
        for m in data[curr]:
            if m not in visited:
                to_visit.append(m)
    return visited


def construct_map(data):
    mapped = defaultdict(list)
    for d in data:
        mapped[d[0]].append(d[1])
        mapped[d[1]].append(d[0])
    return mapped


def test_cuts(data, to_cut):
    ng = copy.deepcopy(data)
    for c in to_cut:
        e, n = c
        if n in ng[e]:
            ng[e].remove(n)
        if e in ng[n]:
            ng[n].remove(e)
    res = bfs(ng)
    if len(res) < len(ng.keys()):
        return len(res) * (len(ng.keys()) - len(res))
    return -1


def plot(data, mapped):
    g = nx.Graph()
    g.add_nodes_from(list(mapped.keys()))

    g.add_edges_from(data)
    pos = nx.spring_layout(g)
    nx.draw(g, pos, with_labels=True, node_color="skyblue", linewidths=1)
    plt.show()


def part1():
    data = read_input()
    data_map = construct_map(data)

    # plot(data, data_map)
    to_cut = [("nvh", "grh"), ("hhx", "vrx"), ("jzj", "vkb")]
    total = test_cuts(data_map, to_cut)
    print(total)


if __name__ == "__main__":
    part1()
