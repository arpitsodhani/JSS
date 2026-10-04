import sys


# --- clause: read_input :: () -> list[tuple[int, int, list[int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        s = data[pos + 1]
        pos += 2
        cases.append((n, s, data[pos:pos + n]))
        pos += n
    return cases


# --- clause: rearrange :: (n: int, s: int, a: list[int]) -> list[int] | None ---
def rearrange(n, s, a):
    total = sum(a)
    if s == total or s > total + 1:
        return None
    zeros = a.count(0)
    twos = a.count(2)
    ones = n - zeros - twos
    return [0] * zeros + [2] * twos + [1] * ones


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, s, a in read_input():
        order = rearrange(n, s, a)
        if order is None:
            out.append("-1")
        else:
            out.append(" ".join(map(str, order)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
