from collections import defaultdict

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

current = defaultdict(int)
for n in lines[0].split(","):
    n = int(n)
    current[n] += 1

population = {}
for i in range(256):
    next = defaultdict(int)
    for k in current:
        if k > 0:
            next[k - 1] += current[k]
        else:
            next[6] += current[k]
            next[8] += current[k]
    current = next
    population[i] = sum(current.values())

p1 = population[79]
p2 = population[255]

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
