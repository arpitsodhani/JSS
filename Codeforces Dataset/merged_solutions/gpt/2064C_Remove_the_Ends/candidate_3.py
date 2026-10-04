# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    p = 1
    ans = []

    for _ in range(t):
        n = data[p]
        p += 1
        a = data[p:p + n]
        p += n

        neg_suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            neg_suffix[i] = neg_suffix[i + 1] + (-a[i] if a[i] < 0 else 0)

        best = neg_suffix[0]
        pos_sum = 0
        for i in range(n):
            if a[i] > 0:
                pos_sum += a[i]
            cur = pos_sum + neg_suffix[i + 1]
            if cur > best:
                best = cur

        ans.append(str(best))

    print("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
