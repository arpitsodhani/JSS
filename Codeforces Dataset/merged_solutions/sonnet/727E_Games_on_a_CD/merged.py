import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    k = int(data[1])
    disc = data[2].decode()
    g = int(data[3])
    names = [data[4 + i].decode() for i in range(g)]
    return n, k, disc, names

# Clause name_lookup [Confidence: 1.00]
def name_lookup(names, k, base, mod):
    lookup = {}
    for index in range(len(names)):
        entry = 0
        for ch in names[index]:
            entry = (entry * base + ord(ch)) % mod
        lookup[entry] = index + 1
    return lookup

# Clause block_owners [Confidence: 1.00]
def block_owners(disc, n, k, lookup, base, mod):
    length = n * k
    text = disc + disc[:k]
    power = pow(base, k, mod)
    rolling = 0
    for i in range(k):
        rolling = (rolling * base + ord(text[i])) % mod
    owners = [0] * length
    owners[0] = lookup.get(rolling, 0)
    for i in range(1, length):
        rolling = (rolling * base + ord(text[i + k - 1]) - power * ord(text[i - 1])) % mod
        owners[i] = lookup.get(rolling, 0)
    return owners

# Clause pick_start [Confidence: 1.00]
def pick_start(owners, n, k, g):
    stamp = [0] * (g + 1)
    for start in range(k):
        mark = start + 1
        picked = []
        for step in range(n):
            who = owners[start + step * k]
            if who == 0 or stamp[who] == mark:
                picked = []
                break
            stamp[who] = mark
            picked.append(who)
        if picked:
            return picked
    return None

# Clause main [Confidence: 1.00]
def main():
    n, k, disc, names = read_input()
    base = 131
    mod = (1 << 61) - 1
    lookup = name_lookup(names, k, base, mod)
    owners = block_owners(disc, n, k, lookup, base, mod)
    picked = pick_start(owners, n, k, len(names))
    if picked is None:
        sys.stdout.write("NO\n")
    else:
        sys.stdout.write("YES\n" + " ".join(map(str, picked)) + "\n")


if __name__ == "__main__":
    main()

