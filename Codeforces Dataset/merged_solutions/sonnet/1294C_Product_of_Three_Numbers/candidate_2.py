import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    return tokens[1:1 + tokens[0]]


# --- clause: split_three :: (n: int) -> tuple[int, int, int] | None ---
def split_three(n):
    a = 0
    d = 2
    while d * d <= n:
        if n % d == 0:
            a = d
            break
        d += 1
    if a == 0:
        return None
    rest = n // a
    b = 0
    d = a + 1
    while d * d < rest:
        if rest % d == 0:
            b = d
            break
        d += 1
    if b == 0:
        return None
    c = rest // b
    if c == b or c == a:
        return None
    return a, b, c


# --- clause: main :: () -> None ---
def main():
    lines = []
    for n in read_input():
        triple = split_three(n)
        if triple is None:
            lines.append("NO")
        else:
            lines.append("YES")
            lines.append("%d %d %d" % triple)
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
