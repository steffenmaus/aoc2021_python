with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def next_east(p):
    x, y = p
    x += 1
    return (x % X, y)


def next_south(p):
    x, y = p
    y += 1
    return (x, y % Y)


X = len(lines[0])
Y = len(lines)

easts = set()
souths = set()
for y in range(0, Y):
    for x in range(0, X):
        p = (x, y)
        match lines[y][x]:
            case ">":
                easts.add(p)
            case "v":
                souths.add(p)

proceed = True

p1 = 0
while proceed:
    proceed = False
    next = set()
    for p in easts:
        q = next_east(p)
        if q not in easts and q not in souths:
            next.add(q)
        else:
            next.add(p)
    if easts != next:
        proceed = True
    easts = next

    next = set()
    for p in souths:
        q = next_south(p)
        if q not in easts and q not in souths:
            next.add(q)
        else:
            next.add(p)
    if souths != next:
        proceed = True
    souths = next
    p1 += 1

print("Part 1: " + str(p1))
