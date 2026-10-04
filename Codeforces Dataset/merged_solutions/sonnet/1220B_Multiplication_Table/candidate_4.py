import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    table = [int(data[i + 1]) for i in range(n * n)]
    return n, table


# --- clause: recover :: (n: int, table: list[int]) -> list[int] ---
def recover(n, table):
    first = table[0 * n + 1] * table[0 * n + 2] // table[1 * n + 2]
    if first < 2:
        root = first
    else:
        lo, hi = 1, 2
        while hi * hi <= first:
            hi *= 2
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if mid * mid <= first:
                lo = mid
            else:
                hi = mid - 1
        root = lo
    values = [root]
    for j in range(1, n):
        values.append(table[0 * n + j] // root)
    return values


# --- clause: main :: () -> None ---
def main():
    n, table = read_input()
    values = recover(n, table)
    sys.stdout.write(" ".join(map(str, values)) + "\n")


if __name__ == "__main__":
    main()
