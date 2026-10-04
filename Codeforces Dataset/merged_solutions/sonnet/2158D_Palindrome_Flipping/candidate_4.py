import sys


# --- clause: read_input :: () -> list[tuple[int, bytes, bytes]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 1
    t = int(data[0])
    cases = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        first = data[pos]
        pos += 1
        second = data[pos]
        pos += 1
        cases.append((n, first, second))
    return cases


# --- clause: reduce_to_zero :: (n: int, bits: list[int]) -> list[tuple[int, int]] ---
def reduce_to_zero(n, bits):
    ops = []
    while True:
        start = -1
        for i in range(n):
            if bits[i] == 1:
                start = i
                break
        if start < 0:
            break
        end = start
        while end + 1 < n and bits[end + 1]:
            end = end + 1
        if end > start:
            for x in range(start, end + 1):
                bits[x] ^= 1
            ops.append((start + 1, end + 1))
            continue
        nxt = -1
        for i in range(start + 1, n):
            if bits[i] == 1:
                nxt = i
                break
        if nxt >= 0:
            for x in range(start, nxt + 1):
                bits[x] ^= 1
            ops.append((start + 1, nxt + 1))
            continue
        if start >= 2:
            finish = ((0, start - 1), (0, start))
        else:
            finish = ((start + 1, n - 1), (start, n - 1))
        for l, r in finish:
            for x in range(l, r + 1):
                bits[x] ^= 1
            ops.append((l + 1, r + 1))
        break
    return ops


# --- clause: solve_case :: (n: int, s: bytes, t: bytes) -> list[tuple[int, int]] ---
def solve_case(n, s, t):
    zero = ord("0")
    left = []
    for byte in s:
        left.append(byte - zero)
    right = []
    for byte in t:
        right.append(byte - zero)
    forward = reduce_to_zero(n, left)
    backward = reduce_to_zero(n, right)
    backward.reverse()
    return forward + backward


# --- clause: main :: () -> None ---
def main():
    out = []
    for case in read_input():
        ops = solve_case(case[0], case[1], case[2])
        out.append(str(len(ops)))
        for l, r in ops:
            out.append(str(l) + " " + str(r))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
