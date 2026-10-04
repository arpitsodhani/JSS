# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    data = sys.stdin.read().strip().split()

    if len(data) > 1:
        n = int(data[0])
        rows = data[1:]
    else:
        s = data[0]
        n = None
        start = 0
        for k in range(1, len(s) + 1):
            x = int(s[:k])
            if len(s) - k == 4 * x * x:
                n = x
                start = k
                break
        rows = [s[start + i * n:start + (i + 1) * n] for i in range(4 * n)]

    cost = []
    for p in range(4):
        c0 = 0
        for i in range(n):
            row = rows[p * n + i]
            for j, ch in enumerate(row):
                expected = (i + j) & 1
                if int(ch) != expected:
                    c0 += 1
        cost.append((c0, n * n - c0))

    ans = 10 ** 18
    for mask in range(16):
        if bin(mask).count("1") == 2:
            cur = 0
            for i in range(4):
                cur += cost[i][1] if (mask >> i) & 1 else cost[i][0]
            ans = min(ans, cur)

    print(ans)

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
