with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

bits = len(lines[0])

epsilon = ""
gamma = ""

for i in range(bits):
    r = [l[i] for l in lines]
    if r.count("1") > r.count("0"):
        epsilon += "1"
        gamma += "0"
    else:
        epsilon += "0"
        gamma += "1"

ox = ""
for i in range(bits):
    r = [l[i] for l in lines if l.startswith(ox)]
    if len(r) == 1:
        ox = [l for l in lines if l.startswith(ox)][0]
        break
    if r.count("1") >= r.count("0"):
        ox += "1"
    else:
        ox += "0"

co2 = ""
for i in range(bits):
    r = [l[i] for l in lines if l.startswith(co2)]
    if len(r) == 1:
        co2 = [l for l in lines if l.startswith(co2)][0]
        break
    if r.count("1") < r.count("0"):
        co2 += "1"
    else:
        co2 += "0"

p1 = int(gamma, 2) * int(epsilon, 2)
p2 = int(ox, 2) * int(co2, 2)

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
