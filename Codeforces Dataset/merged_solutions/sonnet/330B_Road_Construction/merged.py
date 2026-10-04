import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    pairs = []
    pos = 2
    for _ in range(m):
        a = int(data[pos])
        b = int(data[pos + 1])
        pos += 2
        pairs.append((a, b))
    return n, m, pairs

# Clause pick_center [Confidence: 1.00]
def pick_center(n, pairs):
    blocked = [False] * (n + 1)
    for a, b in pairs:
        blocked[a] = True
        blocked[b] = True
    for city in range(1, n + 1):
        if not blocked[city]:
            return city
    return 1

# Clause build_roads [Confidence: 1.00]
def build_roads(n, center):
    roads = []
    for city in range(1, n + 1):
        if city != center:
            roads.append((center, city))
    return roads

# Clause main [Confidence: 1.00]
def main():
    n, m, pairs = read_input()
    center = pick_center(n, pairs)
    roads = build_roads(n, center)
    out = [str(len(roads))]
    for a, b in roads:
        out.append(str(a) + " " + str(b))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

