import re
import sys

with open('input.txt') as file:
    intlines = [[int(n) for n in re.findall(r'-?\d+', line)] for line in file]


def is_in_target(p):
    x, y = p
    return (x_min <= x <= x_max) and (y_min <= y <= y_max)


def could_reach_target(p):
    x, y = p
    if y < y_min:
        return False
    if x > x_max:
        return False
    return True


def f(p, v, peak):
    x, y = p
    dx, dy = v
    if is_in_target(p):
        return peak
    if not could_reach_target(p):
        return None
    x += dx
    y += dy
    dy -= 1
    if dx > 0:
        dx -= 1
    return f((x, y), (dx, dy), max(peak, y))


x_min, x_max, y_min, y_max = intlines[0]

distance = 1
init = 1
while distance < x_min:
    init += 1
    distance += init

p1 = -sys.maxsize
p2 = 0
for dy in range(y_min, - y_min + 1):
    for dx in range(init, x_max + 1):
        res = f((0, 0), (dx, dy), 0)
        if res is not None:
            p1 = max(p1, res)
            p2 += 1

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
