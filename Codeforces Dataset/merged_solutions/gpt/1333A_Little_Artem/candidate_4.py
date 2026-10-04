# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    data = sys.stdin.read().strip().split()
    t = int(data[0])
    idx = 1
    out = []

    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx + 1])
        idx += 2

        for i in range(n):
            row = ['B'] * m
            if i == 0:
                row[0] = 'W'
            out.append(''.join(row))

    print('\n'.join(out))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
