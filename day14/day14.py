from collections import defaultdict

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def get_groups_from_lines(lines):
    groups = []
    group = []
    for l in lines:
        if not l:
            groups.append(group)
            group = []
        else:
            group.append(l)
    groups.append(group)
    return groups


mem = {}


def f(current, deep):
    if (current, deep) in mem:
        return mem[(current, deep)]

    out = defaultdict(int)
    if deep == 0:
        return out
    if len(current) > 2:
        for i, _ in enumerate(current):
            out[current[i]] += 1
            if i > 0:
                for k, v in f(current[i - 1:i + 1], deep).items():
                    out[k] += v
        return out
    else:
        a = current[0]
        b = current[1]
        c = rules[a + b]
        out[c] += 1
        for k, v in f(a + c, deep - 1).items():
            out[k] += v
        for k, v in f(c + b, deep - 1).items():
            out[k] += v
        mem[(current, deep)] = out
        return out


seed, lower = lines[0], lines[2:]
rules = {}
for l in lower:
    a, b = l.split(" -> ")
    rules[a] = b

res1 = f(seed, 10)
res2 = f(seed, 40)
p1 = max(res1.values()) - min(res1.values())
p2 = max(res2.values()) - min(res2.values())

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
