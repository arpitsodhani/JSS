# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys
    from math import gcd

    data = sys.stdin.read().strip().split()
    q = int(data[0])
    ans = []
    idx = 1

    for _ in range(q):
        s = data[idx]
        t = data[idx + 1]
        idx += 2

        l = len(s) * len(t) // gcd(len(s), len(t))
        a = s * (l // len(s))
        b = t * (l // len(t))

        ans.append(a if a == b else "-1")

    print("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
