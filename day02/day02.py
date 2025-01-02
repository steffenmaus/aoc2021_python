with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

h, d = 0, 0
for l in lines:
    a, b = l.split(" ")
    b = int(b)
    match a:
        case "forward":
            h += b
        case "down":
            d += b
        case "up":
            d -= b
p1 = h * d

h, d, aim = 0, 0, 0
for l in lines:
    a, b = l.split(" ")
    b = int(b)
    match a:
        case "forward":
            h += b
            d += aim * b
        case "down":
            aim += b
        case "up":
            aim -= b
p2 = h * d

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
