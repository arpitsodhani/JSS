import sys


# --- clause: read_input :: () -> list[tuple[int, str]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        s = data[pos + 1].decode()
        pos += 2
        cases.append((n, s))
    return cases


# --- clause: build_permutation :: (n: int, s: str) -> list[int] | None ---
def build_permutation(n, s):
    p = [0] * n
    start = 0
    while start < n:
        if s[start] == "1":
            p[start] = start + 1
            start += 1
            continue
        stop = start
        while stop < n and s[stop] == "0":
            stop += 1
        if stop - start < 2:
            return None
        for slot in range(start, stop):
            p[slot] = stop + start - slot
        start = stop
    return p


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, s in read_input():
        p = build_permutation(n, s)
        if p is None:
            out.append("NO")
        else:
            out.append("YES")
            out.append(" ".join(map(str, p)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
