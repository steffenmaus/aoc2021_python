with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def get_all_nei_2d_4(p):
    x, y = p
    r = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]
    return r


def flood_maze(maze, start):
    open = set()
    completed = set()
    open.add(start)
    while open:
        current = open.pop()
        completed.add(current)
        for n in get_all_nei_2d_4(current):
            if n in maze.keys() and n not in completed:
                if maze[n] != 9:
                    open.add(n)
    return completed


X = len(lines[0])
Y = len(lines)

p1 = 0
p2 = 1

maze = {}
for y in range(0, Y):
    for x in range(0, X):
        p = (x, y)
        c = lines[y][x]
        maze[p] = int(c)

solved = set()
sizes = []
for y in range(Y):
    for x in range(X):
        p = (x, y)
        if all([maze[n] > maze[p] for n in get_all_nei_2d_4(p) if n in maze]):
            p1 += 1 + maze[p]
            if p not in solved:
                res = flood_maze(maze, p)
                solved.union(res)
                sizes.append(len(res))

for x in sorted(sizes)[-3:]:
    p2 *= x

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
