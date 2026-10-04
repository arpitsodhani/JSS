import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]


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
    out = []
    for n in read_input():
        triple = split_three(n)
        if triple is None:
            out.append("NO")
        else:
            out.append("YES")
            out.append("%d %d %d" % triple)
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
