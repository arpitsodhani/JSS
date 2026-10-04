import sys


# --- clause: read_input :: () -> list[tuple[int, int, list[int], list[int]]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = fields[cursor]
        m = fields[cursor + 1]
        d = fields[cursor + 2]
        cursor += 3
        p = fields[cursor:cursor + n]
        cursor += n
        a = fields[cursor:cursor + m]
        cursor += m
        cases.append((d, p, a))
    return cases


# --- clause: least_moves :: (d: int, p: list[int], a: list[int]) -> int ---
def least_moves(d, p, a):
    n = len(p)
    where = [0] * (n + 1)
    for i in range(n):
        where[p[i]] = i + 1
    peak = -1
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
        if peak < 0 or cost < peak:
            peak = cost
    if peak < 0:
        return 0
    return peak


# --- clause: main :: () -> None ---
def main():
    out = []
    for d, p, a in read_input():
        out.append(least_moves(d, p, a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
