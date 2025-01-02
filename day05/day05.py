import re
from collections import defaultdict

with open('input.txt') as file:
    intlines = [[int(n) for n in re.findall(r'-?\d+', line)] for line in file]

lvls = defaultdict(int)

for l in intlines:
    x1, y1, x2, y2 = l
    if x1 == x2:
        if y1 > y2:
            y1, y2 = y2, y1
        for y in range(y1, y2 + 1):
            lvls[(x1, y)] += 1
    if y1 == y2:
        if x1 > x2:
            x1, x2 = x2, x1
        for x in range(x1, x2 + 1):
            lvls[(x, y1)] += 1

p1 = 0
for e in lvls.values():
    p1 += e > 1

for l in intlines:
    x1, y1, x2, y2 = l
    if x1 != x2 and y1 != y2:
        dx, dy = 1, 1
        if x1 > x2:
            dx = -1
        if y1 > y2:
            dy = -1
        for t in range(abs(x1 - x2) + 1):
            lvls[(x1 + t * dx, y1 + t * dy)] += 1

p2 = 0
for e in lvls.values():
    p2 += e > 1

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
