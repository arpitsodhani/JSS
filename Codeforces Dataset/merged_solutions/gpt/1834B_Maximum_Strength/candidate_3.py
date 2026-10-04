# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    data = sys.stdin.read().split()
    if not data:
        sys.exit()

    t = int(data[0])
    ans = []
    idx = 1

    for _ in range(t):
        l = data[idx]
        r = data[idx + 1]
        idx += 2

        if len(l) < len(r):
            l = "0" * (len(r) - len(l)) + l
        elif len(r) < len(l):
            r = "0" * (len(l) - len(r)) + r

        res = 0
        n = len(l)
        for i in range(n):
            if l[i] != r[i]:
                res = abs(int(l[i]) - int(r[i])) + 9 * (n - i - 1)
                break

        ans.append(str(res))

    print("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
