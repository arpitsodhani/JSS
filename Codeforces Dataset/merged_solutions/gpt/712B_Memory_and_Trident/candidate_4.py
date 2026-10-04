# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    s = sys.stdin.readline().strip()

    if len(s) % 2:
        print(-1)
    else:
        x = s.count('R') - s.count('L')
        y = s.count('U') - s.count('D')
        print((abs(x) + abs(y)) // 2)

# CLAUSE: finish_program
def main():
    _inner_main()

main()
