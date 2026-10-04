# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    a = data[1:]

    seen = [False] * (n + 1)
    replace = []

    for i, x in enumerate(a):
        if 1 <= x <= n and not seen[x]:
            seen[x] = True
        else:
            replace.append(i)

    missing = [i for i in range(1, n + 1) if not seen[i]]

    for idx, val in zip(replace, missing):
        a[idx] = val

    print(*a)

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
