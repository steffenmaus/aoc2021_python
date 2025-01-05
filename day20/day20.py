with open('sample.txt') as file:
    lines = [line.rstrip() for line in file]


def get_min_max(points):
    min_x = min([p[0] for p in points])
    max_x = max([p[0] for p in points])
    min_y = min([p[1] for p in points])
    max_y = max([p[1] for p in points])
    return min_x, max_x, min_y, max_y


def add_ring_around(points):
    minmax = get_min_max(points)
    for x in range(minmax[0] - 1, minmax[1] + 2):
        points.add((x, minmax[2] - 1))
        points.add((x, minmax[3] + 1))

    for y in range(minmax[2] - 1, minmax[3] + 2):
        points.add((minmax[0] - 1, y))
        points.add((minmax[1] + 1, y))


lookup = lines[0]
lines = lines[2:]

X = len(lines[0])
Y = len(lines)

points = set()
for y in range(0, Y):
    for x in range(0, X):
        p = (x, y)
        if lines[y][x] == "#":
            points.add(p)

p1 = None

for t in range(50):
    if t == 2:
        p1 = len(points)
    next = set()
    minmax = get_min_max(points)
    if lookup[0] == "#" and t % 2 == 1:
        add_ring_around(points)
        add_ring_around(points)
    for y in range(minmax[2] - 1, minmax[3] + 2):
        for x in range(minmax[0] - 1, minmax[1] + 2):
            num = ""
            for dx, dy in ((-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)):
                if (x + dx, y + dy) in points:
                    num += "1"
                else:
                    num += "0"
            if lookup[int(num, 2)] == "#":
                next.add((x, y))
    points = next

p2 = len(points)
print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
