import sys


# --- clause: read_input :: () -> list[tuple[int, int, int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    cases = []
    pos = 1
    for _ in range(t):
        cases.append((data[pos], data[pos + 1], data[pos + 2]))
        pos += 3
    return cases


# --- clause: build_table :: () -> list ---
def build_table():
    big = 1 << 30
    table = [[[big] * 51 for _ in range(31)] for _ in range(31)]
    for n in range(1, 31):
        for m in range(1, 31):
            table[n][m][0] = 0
            room = n * m
            if room < 51:
                table[n][m][room] = 0
    for n in range(1, 31):
        for m in range(1, 31):
            cap = n * m
            if cap > 50:
                cap = 50
            for k in range(1, cap + 1):
                if table[n][m][k] == 0:
                    continue
                best = big
                for cut in range(1, n // 2 + 1):
                    upper = cut * m
                    lower = (n - cut) * m
                    low = k - lower
                    if low < 0:
                        low = 0
                    high = k if k < upper else upper
                    for taken in range(low, high + 1):
                        here = m * m + table[cut][m][taken] + table[n - cut][m][k - taken]
                        if here < best:
                            best = here
                for cut in range(1, m // 2 + 1):
                    upper = cut * n
                    lower = (m - cut) * n
                    low = k - lower
                    if low < 0:
                        low = 0
                    high = k if k < upper else upper
                    for taken in range(low, high + 1):
                        here = n * n + table[n][cut][taken] + table[n][m - cut][k - taken]
                        if here < best:
                            best = here
                table[n][m][k] = best
    return table


# --- clause: main :: () -> None ---
def main():
    table = build_table()
    out = []
    for n, m, k in read_input():
        out.append(str(table[n][m][k]))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
