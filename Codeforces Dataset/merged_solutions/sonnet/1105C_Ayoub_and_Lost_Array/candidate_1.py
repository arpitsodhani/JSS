import sys


# --- clause: read_input :: () -> tuple[int, int, int] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return int(data[0]), int(data[1]), int(data[2])


# --- clause: residue_counts :: (l: int, r: int) -> list[int] ---
def residue_counts(l, r):
    counts = []
    for j in range(3):
        counts.append((r - j) // 3 - (l - 1 - j) // 3)
    return counts


# --- clause: count_arrays :: (n: int, counts: list[int]) -> int ---
def count_arrays(n, counts):
    mod = 1000000007
    ways = [1, 0, 0]
    for _ in range(n):
        nxt = [0, 0, 0]
        for s in range(3):
            here = ways[s]
            if here:
                for j in range(3):
                    t = (s + j) % 3
                    nxt[t] = (nxt[t] + here * counts[j]) % mod
        ways = nxt
    return ways[0] % mod


# --- clause: main :: () -> None ---
def main():
    n, l, r = read_input()
    counts = residue_counts(l, r)
    sys.stdout.write("%d\n" % count_arrays(n, counts))


if __name__ == "__main__":
    main()
