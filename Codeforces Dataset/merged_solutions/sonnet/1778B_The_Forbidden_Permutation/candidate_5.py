import sys


# --- clause: read_input :: () -> list[tuple[int, int, list[int], list[int]]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    offset = 1
    cases = []
    for _ in range(t):
        n = raw[offset]
        m = raw[offset + 1]
        d = raw[offset + 2]
        offset += 3
        p = raw[offset:offset + n]
        offset += n
        a = raw[offset:offset + m]
        offset += m
        cases.append((d, p, a))
    return cases


# --- clause: least_moves :: (d: int, p: list[int], a: list[int]) -> int ---
def least_moves(d, p, a):
    n = len(p)
    where = [0] * (n + 1)
    for i in range(n):
        where[p[i]] = i + 1
    champion = -1
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
        if champion < 0 or cost < champion:
            champion = cost
    if champion < 0:
        return 0
    return champion


# --- clause: main :: () -> None ---
def main():
    out = []
    for d, p, a in read_input():
        out.append(least_moves(d, p, a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
