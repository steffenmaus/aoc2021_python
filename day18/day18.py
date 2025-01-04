import math

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def add_to_first(a, n):
    for i in range(len(a)):
        if a[i].isnumeric():
            old = ""
            j = 0
            while a[i + j].isnumeric():
                old += a[i + j]
                j += 1
            return a[:i] + str(int(old) + n) + a[i + j:]
    return a


def add_to_last(a, n):
    for i in reversed(range(len(a))):
        if a[i].isnumeric():
            old = ""
            j = 0
            while a[i - j].isnumeric():
                old = a[i - j] + old
                j += 1
            return a[:i - j + 1] + str(int(old) + n) + a[i + 1:]
    return a


def explode(a):
    depth = 0
    for i in range(len(a)):
        match a[i]:
            case "[":
                depth += 1
            case "]":
                depth -= 1
        if depth > 4:
            before = a[:i]
            d = 4
            while a[i + d] != "]":
                d += 1
            after = a[i + d + 1:]
            l, r = a[i + 1:i + d].split(",")
            l = int(l)
            r = int(r)
            return add_to_last(before, l) + "0" + add_to_first(after, r)
    return a


def split(a):
    for i in range(len(a)):
        if a[i].isnumeric():
            old = ""
            j = 0
            while a[i + j].isnumeric():
                old += a[i + j]
                j += 1
            if len(old) > 1:
                l = str(int(old) // 2)
                r = str(math.ceil(int(old) / 2))
                return a[:i] + "[" + l + "," + r + "]" + a[i + j:]
    return a


def addition(a, b):
    return reduce("[" + a + "," + b + "]")


def reduce(a):
    b = explode(a)
    if b != a:
        return reduce(b)
    c = split(b)
    if c != b:
        return reduce(c)
    return c


def magnitude(a, pos):
    pos += 1
    if a[pos] == "[":
        l, pos = magnitude(a, pos)
    else:
        l = int(a[pos])
        pos += 1
    pos += 1  # ,
    if a[pos] == "[":
        r, pos = magnitude(a, pos)
    else:
        r = int(a[pos])
        pos += 1
    return l * 3 + r * 2, pos + 1


current = lines[0]
for l in lines[1:]:
    current = addition(current, l)

p1 = magnitude(current, 0)[0]
print("Part 1: " + str(p1))

p2 = 0
for a in lines:
    for b in lines:
        if a != b:
            p2 = max(p2, magnitude(addition(a, b), 0)[0])

print("Part 2: " + str(p2))
