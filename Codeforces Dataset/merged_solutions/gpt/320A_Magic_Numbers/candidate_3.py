# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    s = input().strip()

    i = 0
    ok = True

    while i < len(s):
        if s.startswith("144", i):
            i += 3
        elif s.startswith("14", i):
            i += 2
        elif s.startswith("1", i):
            i += 1
        else:
            ok = False
            break

    print("YES" if ok else "NO")

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
