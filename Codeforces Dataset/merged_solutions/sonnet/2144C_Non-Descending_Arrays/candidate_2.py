import sys

MOD = 998244353


# --- clause: read_input :: () -> list[tuple[list[int], list[int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        a = data[pos:pos + n]
        pos += n
        b = data[pos:pos + n]
        pos += n
        cases.append((a, b))
    return cases

# --- clause: count_subsets :: (a: list[int], b: list[int]) -> int ---
def count_subsets(a, b):
    n = len(a)
    ways = [1, 1]
    for i in range(1, n):
        nxt = [0, 0]
        for before in (0, 1):
            if not ways[before]:
                continue
            left = a[i - 1] if before == 0 else b[i - 1]
            right = b[i - 1] if before == 0 else a[i - 1]
            if left <= a[i] and right <= b[i]:
                nxt[0] = (nxt[0] + ways[before]) % MOD
            if left <= b[i] and right <= a[i]:
                nxt[1] = (nxt[1] + ways[before]) % MOD
        ways = nxt
    return (ways[0] + ways[1]) % MOD

# --- clause: main :: () -> None ---
def main():
    out = []
    for a, b in read_input():
        out.append(str(count_subsets(a, b)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
