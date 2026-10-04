import sys


# --- clause: read_input :: () -> list[tuple[int, bytes, bytes]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    idx = 1
    total = int(data[0])
    cases = []
    for _ in range(total):
        n = int(data[idx])
        cases.append((n, data[idx + 1], data[idx + 2]))
        idx += 3
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
        while end + 1 < n and bits[end + 1] == 1:
            end += 1
        if end > start:
            for x in range(start, end + 1):
                bits[x] ^= 1
            ops.append((start + 1, end + 1))
            continue
        nxt = -1
        for i in range(start + 1, n):
            if bits[i]:
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
        for left, right in finish:
            for x in range(left, right + 1):
                bits[x] ^= 1
            ops.append((left + 1, right + 1))
        break
    return ops


# --- clause: solve_case :: (n: int, s: bytes, t: bytes) -> list[tuple[int, int]] ---
def solve_case(n, s, t):
    zero = ord("0")
    start_bits = [value - zero for value in s]
    goal_bits = [value - zero for value in t]
    forward = reduce_to_zero(n, start_bits)
    backward = reduce_to_zero(n, goal_bits)
    backward.reverse()
    return forward + backward


# --- clause: main :: () -> None ---
def main():
    lines = []
    for n, s, t in read_input():
        ops = solve_case(n, s, t)
        lines.append(str(len(ops)))
        for l, r in ops:
            lines.append("%d %d" % (l, r))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
