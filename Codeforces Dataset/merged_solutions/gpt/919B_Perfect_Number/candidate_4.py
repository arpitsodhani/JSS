# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    k = int(sys.stdin.readline())
    count = 0
    n = 0

    while count < k:
        n += 1
        if sum(map(int, str(n))) == 10:
            count += 1

    print(n)

# CLAUSE: finish_program
def main():
    _inner_main()

main()
