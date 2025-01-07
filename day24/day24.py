from collections import defaultdict

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


# not very efficient, but sufficient
def monad_isolated(pos, z, n):
    current_pos = -1
    r = defaultdict(int)
    r["z"] = z
    for l in lines:
        op = l.split(" ")[0]
        if op == "inp":
            if current_pos == pos:
                return r["z"]
            r[l.split(" ")[1]] = n
            current_pos += 1
        elif current_pos == pos:
            op, a, b = l.split(" ")
            if b not in ("w", "x", "y", "z"):
                v = int(b)
            else:
                v = r[b]
            match op:
                case "add":
                    r[a] += v
                case "mul":
                    r[a] *= v
                case "div":
                    r[a] = r[a] // v
                case "mod":
                    r[a] %= v
                case "eql":
                    if r[a] == v:
                        r[a] = 1
                    else:
                        r[a] = 0
    return r["z"]

# Each part of the program takes z and the current input (n, as w).
# Some of the steps are increasing z, others are conditional decreasing z.
# As we want to end with 0, we can abort as soon as a conditional decrease failed.
# The steps of the program are:
# z0(n0) = n0+14
# z1(n1) = z0*26 + 8 + n1
# z2(n2) = z1*26 + 4 + n2
# z3(n3) = z2*26 + 10 + n3
# z4(n4): if ((z3 - 3 - n3 % 26) == 0): ~z3//26 else: ~z3    ==> only proceed for reduced values !!
# z5(n5): either ~z4 or ~z4//26                              ==> only proceed for reduced values !!
# z6(n6): z5*26 + 4 + n6
# z7(n7): either ~z6 or ~z6//26                              ==> only proceed for reduced values !!
# z8(n8): either ~z7 or ~z7//26                              ==> only proceed for reduced values !!
# z9(n9): either 0 or higher                                 ==> only proceed for 0 !!
# z10(n10): n10 (if z9 is already 0)
# z11(n11): either 0 or higher                               ==> only proceed for 0 !!
# z12(n12): n10+13 (if z11 is already 0)
# z13(n13): either 0 or higher

def f(N, current, z):
    pos = len(current)
    for n in N:
        z_next = None
        match pos:
            case 0:
                z_next = n + 14
            case 1:
                z_next = z * 26 + 8 + n
            case 2:
                z_next = z * 26 + 4 + n
            case 3:
                z_next = z * 26 + 10 + n
            case 4:
                if ((z - 3 - n) % 26) == 0:
                    z_next = (z - 3 - n) // 26
            case 5:
                z_next = monad_isolated(5, z, n)
                if z_next > z // 20:
                    z_next = None
            case 6:
                z_next = z * 26 + 4 + n
            case 7:
                z_next = monad_isolated(7, z, n)
                if z_next > z // 20:
                    z_next = None
            case 8:
                z_next = monad_isolated(8, z, n)
                if z_next > z // 20:
                    z_next = None
            case 9:
                z_next = monad_isolated(9, z, n)
                if z_next != 0:
                    z_next = None
            case 10:
                z_next = n
            case 11:
                z_next = monad_isolated(11, z, n)
                if z_next != 0:
                    z_next = None
            case 12:
                z_next = n + 13
            case 13:
                if monad_isolated(13, z, n) == 0:
                    return current + str(n)
        if z_next is not None:
            res = f(N, current + str(n), z_next)
            if res is not None:
                return res


p1 = f(list(reversed(range(1, 10))), "", None)
p2 = f(range(1, 10), "", None)

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
