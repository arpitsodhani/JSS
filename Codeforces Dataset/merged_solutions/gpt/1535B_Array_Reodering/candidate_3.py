# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys
    from math import gcd

    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    ans = []

    for _ in range(t):
        n = data[idx]
        idx += 1
        a = data[idx:idx + n]
        idx += n

        b = [x for x in a if x % 2 == 0] + [x for x in a if x % 2 == 1]
        cnt = 0

        for i in range(n):
            for j in range(i + 1, n):
                if gcd(b[i], 2 * b[j]) > 1:
                    cnt += 1

        ans.append(str(cnt))

    print("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
