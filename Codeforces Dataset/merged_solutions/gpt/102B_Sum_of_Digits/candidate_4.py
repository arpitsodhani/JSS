# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    n = sys.stdin.readline().strip()
    count = 0

    while len(n) > 1:
        n = str(sum(int(c) for c in n))
        count += 1

    print(count)

# CLAUSE: finish_program
def main():
    _inner_main()

main()
