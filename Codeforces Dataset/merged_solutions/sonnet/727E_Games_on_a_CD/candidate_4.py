import sys


# --- clause: read_input :: () -> tuple[int, int, str, list[str]] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    n = int(numbers[0])
    k = int(numbers[1])
    disc = numbers[2].decode()
    g = int(numbers[3])
    names = [numbers[4 + i].decode() for i in range(g)]
    return n, k, disc, names


# --- clause: name_lookup :: (names: list[str], k: int, base: int, mod: int) -> dict[int, int] ---
def name_lookup(names, k, base, mod):
    lookup = {}
    for index in range(len(names)):
        entry = 0
        for ch in names[index]:
            entry = (entry * base + ord(ch)) % mod
        lookup[entry] = index + 1
    return lookup


# --- clause: block_owners :: (disc: str, n: int, k: int, lookup: dict[int, int], base: int, mod: int) -> list[int] ---
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


# --- clause: pick_start :: (owners: list[int], n: int, k: int, g: int) -> list[int] | None ---
def pick_start(owners, n, k, g):
    stamp = [0 for _ in range(g + 1)]
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


# --- clause: main :: () -> None ---
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
