import re

with open('input.txt') as file:
    intlines = [[int(n) for n in re.findall(r'-?\d+', line)] for line in file]


def has_bingo(board, numbers):
    for r in board:
        if all(n in numbers for n in r):
            return True
    for i in range(5):
        if all(r[i] in numbers for r in board):
            return True
    return False


def calc_score(board, numbers):
    score = 0
    for r in board:
        for n in r:
            if n not in numbers:
                score += n
    return score * numbers[-1]


picks = intlines[0]
intlines = intlines[2:]

boards = []

i = 0
while i < len(intlines):
    boards.append(intlines[i:i + 5])
    i += 6

p1 = None
p2 = None

for i in range(len(picks)):
    current = picks[:i + 1]
    for b in boards:
        if has_bingo(b, current):
            if p1 is None:
                p1 = calc_score(b, current)
            boards.remove(b)
            if not boards:
                p2 = calc_score(b, current)

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
