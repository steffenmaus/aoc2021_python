import re

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def all_ints_in_string(s):
    return [int(n) for n in re.findall(r'-?\d+', s)]


def get_volume(boxes):
    out = 0
    for a in boxes:
        x1a, x2a, y1a, y2a, z1a, z2a = a
        out += (x2a - x1a + 1) * (y2a - y1a + 1) * (z2a - z1a + 1)
    return out


def overlap(a, b):
    x1a, x2a, y1a, y2a, z1a, z2a = a
    x1b, x2b, y1b, y2b, z1b, z2b = b

    x1c, x2c, y1c, y2c, z1c, z2c = None, None, None, None, None, None

    # x_overlap:
    if x1a <= x1b <= x2b <= x2a:
        x1c = x1b
        x2c = x2b
    elif x1b <= x1a <= x2a <= x2b:
        x1c = x1a
        x2c = x2a
    elif x1a <= x1b <= x2a <= x2b:
        x1c = x1b
        x2c = x2a
    elif x1b <= x1a <= x2b <= x2a:
        x1c = x1a
        x2c = x2b
    if x1c is None:
        return None

    # y_overlap:
    if y1a <= y1b <= y2b <= y2a:
        y1c = y1b
        y2c = y2b
    elif y1b <= y1a <= y2a <= y2b:
        y1c = y1a
        y2c = y2a
    elif y1a <= y1b <= y2a <= y2b:
        y1c = y1b
        y2c = y2a
    elif y1b <= y1a <= y2b <= y2a:
        y1c = y1a
        y2c = y2b
    if y1c is None:
        return None

    # z_overlap:
    if z1a <= z1b <= z2b <= z2a:
        z1c = z1b
        z2c = z2b
    elif z1b <= z1a <= z2a <= z2b:
        z1c = z1a
        z2c = z2a
    elif z1a <= z1b <= z2a <= z2b:
        z1c = z1b
        z2c = z2a
    elif z1b <= z1a <= z2b <= z2a:
        z1c = z1a
        z2c = z2b
    if z1c is None:
        return None

    return (x1c, x2c, y1c, y2c, z1c, z2c)


def split(a, c):
    x1a, x2a, y1a, y2a, z1a, z2a = a
    x1c, x2c, y1c, y2c, z1c, z2c = c
    out = []
    xs = sorted([(x1a, x1c - 1), (x1c, x2c), (x2c + 1, x2a)])
    ys = sorted([(y1a, y1c - 1), (y1c, y2c), (y2c + 1, y2a)])
    zs = sorted([(z1a, z1c - 1), (z1c, z2c), (z2c + 1, z2a)])
    for x1, x2 in xs:
        if x1 <= x2:
            for y1, y2 in ys:
                if y1 <= y2:
                    for z1, z2 in zs:
                        if z1 <= z2:
                            b = (x1, x2, y1, y2, z1, z2)
                            if b != c:
                                out.append(b)

    return out


active_boxes = []

for l in lines:
    boxes_to_remove = []
    new_box = tuple(all_ints_in_string(l))
    for a in active_boxes:
        c = overlap(a, new_box)
        if c is not None:
            new_for_a = split(a, c)
            boxes_to_remove.append(a)
            for t in new_for_a:
                active_boxes.append(t)
    if l.startswith("on"):
        active_boxes.append(new_box)
    for t in boxes_to_remove:
        active_boxes.remove(t)

p2 = get_volume(active_boxes)

new_box = (-50, 50, -50, 50, -50, 50)
boxes_to_remove = []
for a in active_boxes:
    c = overlap(a, new_box)
    if c is not None:
        new_for_a = split(a, c)
        boxes_to_remove.append(a)
        for t in new_for_a:
            active_boxes.append(t)
for t in boxes_to_remove:
    active_boxes.remove(t)

p1 = p2 - get_volume(active_boxes)
print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
