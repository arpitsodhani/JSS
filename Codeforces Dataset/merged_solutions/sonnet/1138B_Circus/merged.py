import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    return n, data[1].decode(), data[2].decode()

# Clause group_artists [Confidence: 1.00]
def group_artists(n, clowns, acrobats):
    groups = [[], [], [], []]
    for i in range(n):
        kind = (1 if clowns[i] == "1" else 0) * 2 + (1 if acrobats[i] == "1" else 0)
        spot = 0
        if kind == 2:
            spot = 0
        elif kind == 1:
            spot = 1
        elif kind == 3:
            spot = 2
        else:
            spot = 3
        groups[spot].append(i + 1)
    return groups

# Clause pick_show [Confidence: 1.00]
def pick_show(n, groups):
    na = len(groups[0])
    nb = len(groups[1])
    nc = len(groups[2])
    nd = len(groups[3])
    half = n // 2
    for z in range(nc + 1):
        w = z + half - nb - nc
        if w < 0 or w > nd:
            continue
        need = nb + nc - 2 * z
        if need < 0 or need > na + nb:
            continue
        x = na if na < need else need
        y = need - x
        if y < 0 or y > nb:
            continue
        if x + y + z + w != half:
            continue
        picked = groups[0][:x] + groups[1][:y] + groups[2][:z] + groups[3][:w]
        return picked
    return None

# Clause main [Confidence: 1.00]
def main():
    n, clowns, acrobats = read_input()
    picked = pick_show(n, group_artists(n, clowns, acrobats))
    if picked is None:
        sys.stdout.write("-1\n")
    else:
        sys.stdout.write(" ".join(map(str, picked)) + "\n")


if __name__ == "__main__":
    main()

