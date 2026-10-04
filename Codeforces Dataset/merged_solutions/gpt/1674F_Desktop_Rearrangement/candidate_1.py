# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    input = sys.stdin.buffer.readline
    n, m, q = map(int, input().split())
    total_cells = n * m

    occupied = bytearray(total_cells + 1)
    bit = [0] * (total_cells + 1)
    stars = 0

    for r in range(1, n + 1):
        row = input().strip()
        for c, ch in enumerate(row, 1):
            if ch == 42:
                idx = (c - 1) * n + r
                occupied[idx] = 1
                bit[idx] = 1
                stars += 1

    for i in range(1, total_cells + 1):
        j = i + (i & -i)
        if j <= total_cells:
            bit[j] += bit[i]

    def add(i, v):
        while i <= total_cells:
            bit[i] += v
            i += i & -i

    def prefix_sum(i):
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & -i
        return s

    ans = []
    for _ in range(q):
        r, c = map(int, input().split())
        idx = (c - 1) * n + r

        if occupied[idx]:
            occupied[idx] = 0
            add(idx, -1)
            stars -= 1
        else:
            occupied[idx] = 1
            add(idx, 1)
            stars += 1

        ans.append(str(stars - prefix_sum(stars)))

    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
