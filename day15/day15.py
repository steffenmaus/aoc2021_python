from collections import defaultdict

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def get_all_nei_2d_4(p):
    x, y = p
    r = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]
    return r


def get_distances(maze):
    distances = defaultdict(list)
    for p in maze:
        for n in get_all_nei_2d_4(p):
            if n in maze:
                distances[p].append((n, maze[n]))
    return distances


import heapq


def dijkstra(start, target, distances):
    out = {}
    out[start] = 0
    Q = []
    for nei in distances[start]:
        node, dist = nei
        heapq.heappush(Q, (dist, node, start))
    while target not in out:
        dist, current, prev = heapq.heappop(Q)
        if current not in out.keys():
            out[current] = dist
            for nei in distances[current]:
                n, d = nei
                heapq.heappush(Q, (d + dist, n, current))
    return out[target]


X = len(lines[0])
Y = len(lines)

maze = {}
maze2 = {}
for y in range(0, Y):
    for x in range(0, X):
        p = (x, y)
        c = lines[y][x]
        maze[p] = int(c)

        for dx in range(5):
            for dy in range(5):
                p2 = (x + dx * X, y + dy * Y)
                v = (int(c) + dx + dy)
                if v > 9:
                    v -= 9
                maze2[p2] = v

start = (0, 0)
target = (X - 1, Y - 1)
target2 = (5 * X - 1, 5 * Y - 1)

p1 = dijkstra(start, target, get_distances(maze))
print("Part 1: " + str(p1))

p2 = dijkstra(start, target2, get_distances(maze2))
print("Part 2: " + str(p2))
