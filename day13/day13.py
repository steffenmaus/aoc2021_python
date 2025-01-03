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


def draw_points(points):
    min_x = min([p[0] for p in points])
    max_x = max([p[0] for p in points])
    min_y = min([p[1] for p in points])
    max_y = max([p[1] for p in points])
    for y in range(min_y, max_y + 1):
        line = ""
        for x in range(min_x, max_x + 1):
            if (x, y) in points:
                line += "█"
            else:
                line += " "
        print(line)


upper, lower = get_groups_from_lines(lines)

dots = set()
for l in upper:
    a, b = l.split(",")
    dots.add((int(a), int(b)))

p1 = None
for l in lower:
    axis = l.split("=")[0][-1]
    val = int(l.split("=")[1])
    new_dots = set()

    for p in dots:
        x, y = p
        if axis == "y":
            if y < val:
                new_dots.add(p)
            else:
                new_dots.add((x, 2 * val - y))
        else:
            if x < val:
                new_dots.add(p)
            else:
                new_dots.add((2 * val - x, y))

    dots = new_dots
    if p1 is None:
        p1 = len(dots)

print("Part 1: " + str(p1))
print("Part 2: ")
draw_points(dots)
