# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    s = sys.stdin.readline().strip()

    boys = 0
    ans = 0

    for c in s:
        if c == 'M':
            boys += 1
        elif boys:
            ans = max(ans + 1, boys)

    print(ans)

# CLAUSE: finish_program
def main():
    _inner_main()

main()
