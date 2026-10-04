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
    blocks = []
    i = 0
    while i < n:
        if s[i] == "1":
            i += 1
            continue
        j = i
        while j < n and s[j] == "0":
            j += 1
        if j - i == 1:
            return None
        blocks.append((i, j))
        i = j
    p = list(range(1, n + 1))
    for start, stop in blocks:
        for slot in range(start, stop - 1):
            p[slot] = slot + 2
        p[stop - 1] = start + 1
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
