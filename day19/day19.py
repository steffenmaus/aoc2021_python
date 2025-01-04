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


def get_all_orientations(id):
    if id in mem:
        return mem[id]
    beacons = scanners[id]
    out = []
    for rx in range(4):
        for ry in range(4):
            for rz in range(4):
                temp = set()
                for b in beacons:
                    x, y, z = b
                    for _ in range(rx):
                        y, z = z, -y
                    for _ in range(ry):
                        x, z = -z, x
                    for _ in range(rz):
                        x, y = y, -x
                    temp.add((x, y, z))
                if not temp in out:
                    out.append(temp)
    mem[id] = out
    return out


done = set()


def find_next():
    for sk in solved:
        for s in scanners:
            if s not in solved:
                if (sk,s) not in done:
                    done.add((sk,s))
                    for o in get_all_orientations(s):
                        a = solved[sk]
                        for p in a:
                            for q in o:
                                dx = q[0] - p[0]
                                dy = q[1] - p[1]
                                dz = q[2] - p[2]
                                b = set()
                                for q2 in o:
                                    b.add((q2[0] - dx, q2[1] - dy, q2[2] - dz))
                                if len(a.intersection(b)) >= +12:
                                    return s, b, (dx, dy, dz)


scanners = {}
for g in get_groups_from_lines(lines):
    id = int(g[0].split(" ")[2])
    beacons = set()
    for l in g[1:]:
        x, y, z = list(map(int, l.split(",")))
        beacons.add((x, y, z))
    scanners[id] = beacons

solved = {}
solved[0] = scanners[0]

positions = {}
positions[0] = (0, 0, 0)

beacons = set()
beacons.update(solved[0])

while len(solved) != len(scanners):
    print("Progress: " + str(len(solved)) + "/" + str(len(scanners)))
    res = find_next()
    solved[res[0]] = res[1]
    positions[res[0]] = res[2]
    beacons.update(res[1])

p1 = len(beacons)
p2 = 0
for p in positions.values():
    for q in positions.values():
        dx = abs(p[0] - q[0])
        dy = abs(p[1] - q[1])
        dz = abs(p[2] - q[2])
        d = dx + dy + dz
        p2 = max(p2, d)

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
