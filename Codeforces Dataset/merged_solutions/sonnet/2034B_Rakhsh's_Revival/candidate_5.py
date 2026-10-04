import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, bytes]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        m = int(data[pos + 1])
        k = int(data[pos + 2])
        s = bytes(data[pos + 3])
        pos += 4
        cases.append((n, m, k, s))
    return cases


# --- clause: timar_uses :: (n: int, m: int, k: int, s: bytes) -> int ---
def timar_uses(n, m, k, s):
    used = 0
    start = 0
    while start < n:
        if s[start] != 48:
            start += 1
            continue
        stop = start
        while stop < n and s[stop] != 49:
            stop += 1
        cursor = start
        while stop - cursor >= m:
            used += 1
            cursor += m - 1 + k
        start = stop
    return used


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, m, k, s in read_input():
        out.append(str(timar_uses(n, m, k, s)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
