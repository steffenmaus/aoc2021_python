with open('input.txt') as file:
    lines = [int(line.rstrip()) for line in file]

p1 = 0
p2 = 0

for i, _ in enumerate(lines):
    if i > 0:
        p1 += lines[i] > lines[i - 1]
    if i > 2:
        a = sum(lines[i - 3:i])
        b = sum(lines[i - 2:i + 1])
        p2 += b > a

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
