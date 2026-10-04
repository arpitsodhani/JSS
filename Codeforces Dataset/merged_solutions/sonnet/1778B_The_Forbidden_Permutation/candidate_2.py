import sys


# --- clause: read_input :: () -> list[tuple[int, int, list[int], list[int]]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    t = tokens[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = tokens[pos]
        m = tokens[pos + 1]
        d = tokens[pos + 2]
        pos += 3
        p = tokens[pos:pos + n]
        pos += n
        a = tokens[pos:pos + m]
        pos += m
        cases.append((d, p, a))
    return cases


# --- clause: least_moves :: (d: int, p: list[int], a: list[int]) -> int ---
def least_moves(d, p, a):
    n = len(p)
    where = [0] * (n + 1)
    for i in range(n):
        where[p[i]] = i + 1
    top = -1
    for i in range(len(a) - 1):
        x = where[a[i]]
        y = where[a[i + 1]]
        if x >= y or y > x + d:
            return 0
        cost = y - x
        room = (x - 1) + (n - y)
        need = d + 1 - cost
        if need <= room and need < cost:
            cost = need
        if top < 0 or cost < top:
            top = cost
    if top < 0:
        return 0
    return top


# --- clause: main :: () -> None ---
def main():
    out = []
    for d, p, a in read_input():
        out.append(least_moves(d, p, a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
