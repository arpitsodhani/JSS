# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys
    from collections import Counter

    lines = sys.stdin.read().splitlines()
    s1 = lines[0] if len(lines) > 0 else ""
    s2 = lines[1] if len(lines) > 1 else ""

    available = Counter(c for c in s1 if c != ' ')
    needed = Counter(c for c in s2 if c != ' ')

    print("YES" if all(available[ch] >= cnt for ch, cnt in needed.items()) else "NO")

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
