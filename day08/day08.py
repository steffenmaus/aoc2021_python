with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

p1 = 0
p2 = 0

for l in lines:
    a, b = l.split(" | ")
    a = a.split(" ")
    b = b.split(" ")

    for x in b:
        p1 += len(x) in (2, 4, 3, 7)

    lookup = {}
    while len(lookup) < 10:
        for x in a:
            if len(x) == 6 and 7 in lookup and 9 in lookup and all([y in x for y in lookup[7]]):
                lookup[0] = set(x)
                a.remove(x)
            elif len(x) == 2:
                lookup[1] = set(x)
                a.remove(x)
            elif len(lookup) == 9:
                lookup[2] = set(x)
                a.remove(x)
            elif len(x) == 5 and 7 in lookup and all([y in x for y in lookup[7]]):
                lookup[3] = set(x)
                a.remove(x)
            elif len(x) == 4:
                lookup[4] = set(x)
                a.remove(x)
            elif len(x) == 5 and 3 in lookup and 9 in lookup and all([y in lookup[9] for y in x]):
                lookup[5] = set(x)
                a.remove(x)
            elif len(x) == 6 and 0 in lookup and 9 in lookup:
                lookup[6] = set(x)
                a.remove(x)
            elif len(x) == 3:
                lookup[7] = set(x)
                a.remove(x)
            elif len(x) == 7:
                lookup[8] = set(x)
                a.remove(x)
            elif len(x) == 6 and 4 in lookup and all([y in x for y in lookup[4]]):
                lookup[9] = set(x)
                a.remove(x)
    out = ""
    for x in b:
        for k, v in lookup.items():
            if set(x) == v:
                out += str(k)

    p2 += int(out)

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
