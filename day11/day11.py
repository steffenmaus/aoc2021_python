with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def get_all_nei_2d_8(p):
    x, y = p
    out = []
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx != 0 or dy != 0:
                out.append((x + dx, y + dy))
    return out


X = len(lines[0])
Y = len(lines)

maze = {}
for y in range(0, Y):
    for x in range(0, X):
        p = (x, y)
        c = lines[y][x]
        maze[p] = int(c)

p1 = 0
p2 = None
step = 0
while p2 is None:
    flashed = set()
    queue = []
    for y in range(Y):
        for x in range(X):
            queue.append((x, y))
    while queue:
        p = queue.pop()
        if p not in flashed:
            maze[p] += 1
            if maze[p] > 9:
                maze[p] = 0
                flashed.add(p)
                for n in get_all_nei_2d_8(p):
                    if n in maze.keys():
                        queue.append(n)
    if len(flashed) == 100:
        p2 = step + 1
    if step < 100:
        p1 += len(flashed)
    step += 1

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
