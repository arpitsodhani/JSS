# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = sys.stdin.buffer.read().split()
    p = 0
    n = int(data[p])
    m = int(data[p + 1])
    k = int(data[p + 2])
    p += 3

    pref = []
    for _ in range(k):
        cnt = int(data[p])
        p += 1
        grid = [[0] * (m + 1) for _ in range(n + 1)]
        for _ in range(cnt):
            r = int(data[p])
            c = int(data[p + 1])
            v = int(data[p + 2])
            p += 3
            grid[r][c] = v

        for r in range(1, n + 1):
            row = grid[r]
            prev = grid[r - 1]
            acc = 0
            for c in range(1, m + 1):
                acc += row[c]
                row[c] = acc + prev[c]
        pref.append(grid)

    q = int(data[p])
    p += 1
    active = [1] * k
    ans = []

    for _ in range(q):
        typ = data[p]
        if typ == b"SWITCH":
            g = int(data[p + 1]) - 1
            p += 2
            active[g] ^= 1
        else:
            r1 = int(data[p + 1])
            c1 = int(data[p + 2])
            r2 = int(data[p + 3])
            c2 = int(data[p + 4])
            p += 5
            r0 = r1 - 1
            c0 = c1 - 1
            total = 0
            for i, table in enumerate(pref):
                if active[i]:
                    total += table[r2][c2] - table[r0][c2] - table[r2][c0] + table[r0][c0]
            ans.append(str(total))

    sys.stdout.write("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
