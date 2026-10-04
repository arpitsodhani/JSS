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
            room = n * m
            table[n][m][0] = 0
            if room <= 50:
                table[n][m][room] = 0
    for n in range(1, 31):
        for m in range(1, 31):
            limit = n * m
            if limit > 50:
                limit = 50
            for k in range(1, limit + 1):
                if table[n][m][k] == 0:
                    continue
                best = 1 << 30
                for cut in range(1, (n >> 1) + 1):
                    price = m * m
                    top = cut * m
                    for taken in range(0, k + 1):
                        if taken > top or k - taken > (n - cut) * m:
                            continue
                        here = price + table[cut][m][taken] + table[n - cut][m][k - taken]
                        if here < best:
                            best = here
                for cut in range(1, m // 2 + 1):
                    price = n * n
                    left = cut * n
                    for taken in range(0, k + 1):
                        if taken > left or k - taken > (m - cut) * n:
                            continue
                        here = price + table[n][cut][taken] + table[n][m - cut][k - taken]
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
