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
    p = list(range(1, n + 1))
    index = 0
    while index < n:
        if s[index] == "1":
            index += 1
            continue
        end = index
        while end < n and s[end] == "0":
            end += 1
        width = end - index
        if width == 1:
            return None
        for offset in range(width):
            p[index + offset] = index + (offset + 1) % width + 1
        index = end
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
