# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    from itertools import combinations
    import sys

    a = list(map(int, sys.stdin.read().split()))
    total = sum(a)

    ok = False
    for comb in combinations(range(6), 3):
        if sum(a[i] for i in comb) * 2 == total:
            ok = True
            break

    print("YES" if ok else "NO")

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
