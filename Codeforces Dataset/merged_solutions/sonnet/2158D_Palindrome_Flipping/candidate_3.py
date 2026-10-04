import sys


# --- clause: read_input :: () -> list[tuple[int, bytes, bytes]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    while len(cases) < t:
        n = int(data[pos])
        first = data[pos + 1]
        second = data[pos + 2]
        pos += 3
        cases.append((n, first, second))
    return cases


# --- clause: reduce_to_zero :: (n: int, bits: list[int]) -> list[tuple[int, int]] ---
def reduce_to_zero(n, bits):
    ops = []
    while True:
        start = -1
        for i in range(n):
            if bits[i]:
                start = i
                break
        if start < 0:
            break
        end = start
        while end + 1 < n and bits[end + 1]:
            end += 1
        if end > start:
            for x in range(start, end + 1):
                bits[x] = 1 - bits[x]
            ops.append((start + 1, end + 1))
            continue
        nxt = -1
        for i in range(start + 1, n):
            if bits[i]:
                nxt = i
                break
        if nxt >= 0:
            for x in range(start, nxt + 1):
                bits[x] = 1 - bits[x]
            ops.append((start + 1, nxt + 1))
            continue
        if start >= 2:
            finish = ((0, start - 1), (0, start))
        else:
            finish = ((start + 1, n - 1), (start, n - 1))
        for l, r in finish:
            for x in range(l, r + 1):
                bits[x] = 1 - bits[x]
            ops.append((l + 1, r + 1))
        break
    return ops


# --- clause: solve_case :: (n: int, s: bytes, t: bytes) -> list[tuple[int, int]] ---
def solve_case(n, s, t):
    zero = ord("0")
    left = [byte - zero for byte in s]
    right = [byte - zero for byte in t]
    forward = reduce_to_zero(n, left)
    backward = reduce_to_zero(n, right)
    backward.reverse()
    return forward + backward


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, s, t in read_input():
        ops = solve_case(n, s, t)
        out.append(str(len(ops)))
        for l, r in ops:
            out.append(str(l) + " " + str(r))
    print("\n".join(out))


if __name__ == "__main__":
    main()
