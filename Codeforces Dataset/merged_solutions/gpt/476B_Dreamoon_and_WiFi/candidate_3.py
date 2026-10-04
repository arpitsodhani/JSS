# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys
    from math import comb

    s1, s2 = sys.stdin.read().split()

    target = s1.count('+') - s1.count('-')
    known = s2.count('+') - s2.count('-')
    q = s2.count('?')

    need = target - known

    if (q + need) % 2 != 0 or abs(need) > q:
        print("0.000000000000")
    else:
        plus_needed = (q + need) // 2
        print(f"{comb(q, plus_needed) / (2 ** q):.12f}")

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
