import numpy as np
import sympy as sp
import itertools


def read_input():
    with open("input.txt") as f:
        lines = f.read().splitlines()
        points = []
        for l in lines:
            point, velocity = l.split("@")
            point = tuple([int(p.strip()) for p in point.split(", ")])
            velocity = tuple([int(p.strip()) for p in velocity.split(", ")])
            points.append((point, velocity))

        return points


def line_from_point(pv):
    point, velocity = pv
    a = velocity[1]
    b = -velocity[0]
    c = a * (point[0]) + b * (point[1])
    return a / -b, c / b


def line_3d_from_point(pv):
    point, velocity = pv
    a = velocity[1]
    b = velocity[0]
    c = -velocity[2]
    d = a * point[0] + b * point[1] + c * point[2]
    return a / -c, b / -c, d / c


def part1():
    points = read_input()
    combos = list(itertools.combinations(points, 2))
    borders = [200000000000000, 400000000000000]
    total = 0
    for combo in combos:
        m1, c1 = line_from_point(combo[0])
        m2, c2 = line_from_point(combo[1])

        a = np.array([[-m1, 1], [-m2, 1]])
        b = np.array([c1, c2])

        try:
            x = np.linalg.solve(a, b)
            if (
                x[0] >= borders[0]
                and x[0] <= borders[1]
                and x[1] >= borders[0]
                and x[1] <= borders[1]
            ):
                if (
                    x[0] > combo[0][0][0]
                    and combo[0][1][0] <= 0
                    or x[0] < combo[0][0][0]
                    and combo[0][1][0] >= 0
                ):
                    continue
                if (
                    x[1] > combo[0][0][1]
                    and combo[0][1][1] <= 0
                    or x[1] < combo[0][0][1]
                    and combo[0][1][1] >= 0
                ):
                    continue
                if (
                    x[0] > combo[1][0][0]
                    and combo[1][1][0] <= 0
                    or x[0] < combo[1][0][0]
                    and combo[1][1][0] >= 0
                ):
                    continue
                if (
                    x[1] > combo[1][0][1]
                    and combo[1][1][1] <= 0
                    or x[1] < combo[1][0][1]
                    and combo[1][1][1] >= 0
                ):
                    continue
                total += 1
        except np.linalg.LinAlgError:
            continue

    print(total)

    # [print(p) for p in points]


def sum_vel(pv):
    point, velocity = pv
    res = []
    for i in range(350):
        res.append(
            (
                point[0] + velocity[0] * i,
                point[1] + velocity[1] * i,
                point[2] + velocity[2] * i,
            )
        )
    return res


def part2():
    points = read_input()

    equations = []
    for p in points:
        pl = list(p[0]) + list(p[1])
        vx, vy, vz = sp.symbols("vx,vy,vz")
        x, y, z = sp.symbols("x,y,z")
        equations.append(sp.Eq((pl[0] - x) * (vy - pl[4]), (pl[1] - y) * (vx - pl[3])))
        equations.append(sp.Eq((pl[0] - x) * (vz - pl[5]), (pl[2] - z) * (vx - pl[3])))
    solution = sp.solve(equations, [vx, vy, vz, x, y, z])
    print(sum(solution[0][3:]))


if __name__ == "__main__":
    part1()
    part2()
