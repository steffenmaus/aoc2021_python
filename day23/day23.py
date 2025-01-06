import heapq

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def get_all_nei_2d_4(p):
    x, y = p
    r = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]
    return r


def steps_in_maze(start, blocked):
    out = {}
    border = set()
    border.add(start)
    completed = set()
    steps = 0
    while border:
        next_border = set()
        completed.update(border)
        for p in border:
            out[p] = steps
            x, y = p
            if (x, y - 1) in out:
                out.pop((x, y - 1))
            for n in get_all_nei_2d_4(p):
                if n in FLOOR and n not in completed and n not in blocked:
                    next_border.add(n)
        border = next_border
        steps += 1
    out.pop(start)
    for r in RESTRICTED:
        if r in out:
            out.pop(r)
    return out


def get_neighbors(state, part2):
    blocked = set(state)
    size = 2
    if part2:
        size = 4
    a = state[size * 0 + 0:size * 0 + size]
    b = state[size * 1 + 0:size * 1 + size]
    c = state[size * 2 + 0:size * 2 + size]
    d = state[size * 3 + 0:size * 3 + size]
    current = [a, b, c, d]

    out = []

    for i, cu in enumerate(current):
        others = blocked.difference(cu)
        target = TARGETS[i]
        if not cu == TARGETS[i]:
            for j, p in enumerate(cu):
                steps = steps_in_maze(p, blocked)
                for t in steps:
                    if t in UPPER or t in target:
                        if (p in UPPER) != (t in UPPER):
                            if not (t in UPPER and p in target and all([o not in target for o in others])):
                                if not (t in target and any([o in target for o in others])):
                                    next = list(cu)
                                    next[j] = t
                                    left = state[:size * i]
                                    right = state[i * size + size:]
                                    next_state = tuple(left) + tuple(next) + tuple(right)
                                    out.append((next_state, steps[t] * 10 ** i))

    return out


def dijkstra(start, part2):
    A, B, C, D = TARGETS
    size = 2
    if part2:
        size = 4
    out = {}
    out[start] = 0
    Q = []
    for nei in get_neighbors(start, part2):
        node, dist = nei
        heapq.heappush(Q, (dist, node, start))
    while True:
        dist, current, prev = heapq.heappop(Q)
        if current not in out.keys():
            a = current[size * 0 + 0:size * 0 + size]
            b = current[size * 1 + 0:size * 1 + size]
            c = current[size * 2 + 0:size * 2 + size]
            d = current[size * 3 + 0:size * 3 + size]
            if set(a) == A and set(b) == B and set(c) == C and set(d) == D:
                return dist
            out[current] = dist
            for nei in get_neighbors(current, part2):
                n, d = nei
                heapq.heappush(Q, (d + dist, n, current))


def f(part2):
    ambers = []
    bronzes = []
    coppers = []
    deserts = []
    if part2:
        lines.insert(3, "  #D#B#A#C#")
        lines.insert(3, "  #D#C#B#A#")
    for y in range(0, len(lines)):
        for x in range(0, len(lines[y])):
            p = (x, y)
            match lines[y][x]:
                case "A":
                    ambers.append(p)
                case "B":
                    bronzes.append(p)
                case "C":
                    coppers.append(p)
                case "D":
                    deserts.append(p)
    global FLOOR, TARGETS, RESTRICTED, UPPER
    RESTRICTED = {(3, 1), (5, 1), (7, 1), (9, 1)}
    UPPER = {(1, 1), (2, 1), (4, 1), (6, 1), (8, 1), (10, 1), (11, 1)}
    FLOOR = set()
    FLOOR.update(RESTRICTED)
    FLOOR.update(UPPER)
    FLOOR.update(ambers)
    FLOOR.update(bronzes)
    FLOOR.update(coppers)
    FLOOR.update(deserts)
    start = tuple(ambers + bronzes + coppers + deserts)
    if part2:
        A = {(3, 2), (3, 3), (3, 4), (3, 5)}
        B = {(5, 2), (5, 3), (5, 4), (5, 5)}
        C = {(7, 2), (7, 3), (7, 4), (7, 5)}
        D = {(9, 2), (9, 3), (9, 4), (9, 5)}
    else:
        A = {(3, 2), (3, 3)}
        B = {(5, 2), (5, 3)}
        C = {(7, 2), (7, 3)}
        D = {(9, 2), (9, 3)}
    TARGETS = [A, B, C, D]

    return dijkstra(start, part2)


p1 = f(False)
print("Part 1: " + str(p1))

p2 = f(True)
print("Part 2: " + str(p2))
