import sys

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def f(n):
    return n * (n + 1) // 2


ints = list(map(int, lines[0].split(",")))

p1 = sys.maxsize
p2 = sys.maxsize
for target in range(min(ints), max(ints) + 1):
    fuel = 0
    fuel2 = 0
    for i in ints:
        fuel += abs(i - target)  # median
        fuel2 += f(abs(i - target))
    p1 = min(fuel, p1)
    p2 = min(fuel2, p2)

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
