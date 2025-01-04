with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def parse_packet(pos):
    version = int(definition[pos:pos + 3], 2)
    pos += 3
    type_id = int(definition[pos:pos + 3], 2)
    pos += 3
    sub_packets = []
    literal_value = None
    match type_id:
        case 4:
            literal_bin = ""
            while not literal_bin or definition[pos - 5] == "1":
                literal_bin += definition[pos + 1:pos + 5]
                pos += 5
            literal_value = int(literal_bin, 2)
        case _:
            length_type = definition[pos]
            pos += 1
            if length_type == "0":
                total_length_in_bits = int(definition[pos:pos + 15], 2)
                pos += 15
                target_pos = pos + total_length_in_bits
                while pos < target_pos:
                    sub_packets.append(parse_packet(pos))
                    pos = sub_packets[-1][4]
            else:
                n_of_subpackets = int(definition[pos:pos + 11], 2)
                pos += 11
                for _ in range(n_of_subpackets):
                    sub_packets.append(parse_packet(pos))
                    pos = sub_packets[-1][4]
    return (version, type_id, sub_packets, literal_value, pos)


def f1(package):
    out = package[0]
    for s in package[2]:
        out += f1(s)
    return out


def f2(package):
    if package[1] == 4:
        return package[3]
    else:
        res = [f2(s) for s in package[2]]
        match package[1]:
            case 0:
                return sum(res)
            case 1:
                out = 1
                for r in res:
                    out *= r
                return out
            case 2:
                return min(res)
            case 3:
                return max(res)
            case 5:
                if res[0] > res[1]:
                    return 1
                else:
                    return 0
            case 6:
                if res[0] < res[1]:
                    return 1
                else:
                    return 0
            case 7:
                if res[0] == res[1]:
                    return 1
                else:
                    return 0


hex = lines[0]
definition = str(bin(int(hex, 16))[2:]).zfill(len(hex) * 4)

root = parse_packet(0)

p1 = f1(root)
p2 = f2(root)

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
