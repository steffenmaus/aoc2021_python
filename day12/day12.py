from collections import defaultdict

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def f(current, path, bonus):
    if current == "end":
        return 1
    if current == "start" and path != "":
        return 0
    else:
        out = 0
        for n in nei[current]:
            regular = n.isupper() or n not in path
            if regular or bonus:
                out += f(n, path + current, regular & bonus)
        return out


nei = defaultdict(list)

for l in lines:
    a, b = l.split("-")
    nei[a].append(b)
    nei[b].append(a)

p1 = f("start", "", False)
p2 = f("start", "", True)

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
