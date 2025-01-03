with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

costs = {}
costs[")"] = 3
costs["]"] = 57
costs["}"] = 1197
costs[">"] = 25137

costs2 = {}
costs2["("] = 1
costs2["["] = 2
costs2["{"] = 3
costs2["<"] = 4

opens = {}
opens[")"] = "("
opens["]"] = "["
opens["}"] = "{"
opens[">"] = "<"


def calc_score(chars):
    score = 0
    for c in chars:
        score *= 5
        score += costs2[c]
    return score


p1 = 0
all_scores = []
for l in lines:
    stack = []
    corrupt = False
    for c in l:
        if c not in opens:
            stack.append(c)
        else:
            if stack.pop() != opens[c]:
                corrupt = True
                p1 += costs[c]
    if not corrupt:
        all_scores.append(calc_score("".join(reversed(stack))))

p2 = sorted(all_scores)[len(all_scores) // 2]

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
