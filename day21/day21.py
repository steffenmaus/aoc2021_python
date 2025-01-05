with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


class DeterministicDice:
    def __init__(self, sided):
        self.sided = sided
        self.next = 1
        self.usage = 0

    def get_usage(self):
        return self.usage

    def roll(self):
        self.usage += 1
        out = self.next
        self.next += 1
        if self.next > self.sided:
            self.next -= self.sided
        return out


mem = {}


def f(pos1, sc1, pos2, sc2, player):
    if (pos1, sc1, pos2, sc2, player) in mem:
        return mem[(pos1, sc1, pos2, sc2, player)]
    if sc1 >= 21:
        return [1, 0]
    if sc2 >= 21:
        return [0, 1]
    else:
        win1, win2 = 0, 0
        for d1 in (1, 2, 3):
            for d2 in (1, 2, 3):
                for d3 in (1, 2, 3):
                    if player == 1:
                        n_pos1 = pos1 + d1 + d2 + d3
                        while n_pos1 > 10:
                            n_pos1 -= 10
                        n_sc1 = sc1 + n_pos1
                        res = f(n_pos1, n_sc1, pos2, sc2, 2)
                    else:
                        n_pos2 = pos2 + d1 + d2 + d3
                        while n_pos2 > 10:
                            n_pos2 -= 10
                        n_sc2 = sc2 + n_pos2
                        res = f(pos1, sc1, n_pos2, n_sc2, 1)
                    win1 += res[0]
                    win2 += res[1]
        mem[(pos1, sc1, pos2, sc2, player)] = [win1, win2]
        return [win1, win2]


pos = {}
pos[0] = int(lines[0][-1])
pos[1] = int(lines[1][-1])

scores = {}
scores[0] = 0
scores[1] = 0

player = 0
dice = DeterministicDice(100)
while max(scores.values()) < 1000:
    vals = []
    for _ in range(3):
        vals.append(dice.roll())
    steps = sum(vals)
    pos[player] += steps
    while pos[player] > 10:
        pos[player] -= 10
    scores[player] += pos[player]

    player += 1
    player %= 2

p1 = min(scores.values()) * dice.get_usage()
p2 = max(f(int(lines[0][-1]), 0, int(lines[1][-1]), 0, 1))

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
