# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def build_prefix(rows, n, m):
    for r in range(1, n + 1):
        current = rows[r]
        upper = rows[r - 1]
        for c in range(1, m + 1):
            current[c] += current[c - 1] + upper[c] - upper[c - 1]
    return rows

def main():
    parts = sys.stdin.buffer.read().split()
    at = 0

    n, m, k = map(int, parts[at:at + 3])
    at += 3

    sums = []
    for _ in range(k):
        bulbs = int(parts[at])
        at += 1
        rows = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        end = at + bulbs * 3
        while at < end:
            r = int(parts[at])
            c = int(parts[at + 1])
            val = int(parts[at + 2])
            rows[r][c] = val
            at += 3
        sums.append(build_prefix(rows, n, m))

    queries = int(parts[at])
    at += 1

    mask = (1 << k) - 1
    lines = []

    for _ in range(queries):
        if parts[at] == b"SWITCH":
            g = int(parts[at + 1]) - 1
            mask ^= 1 << g
            at += 2
        else:
            r1 = int(parts[at + 1])
            c1 = int(parts[at + 2])
            r2 = int(parts[at + 3])
            c2 = int(parts[at + 4])
            at += 5

            total = 0
            bitset = mask
            while bitset:
                low = bitset & -bitset
                gi = low.bit_length() - 1
                pref = sums[gi]
                total += pref[r2][c2] - pref[r1 - 1][c2] - pref[r2][c1 - 1] + pref[r1 - 1][c1 - 1]
                bitset -= low
            lines.append(str(total))

    sys.stdout.write("\n".join(lines))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
