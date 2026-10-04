# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    cases = next(it)
    result = []
    for _ in range(cases):
        n = next(it)
        m = next(it)
        r = next(it)
        c = next(it)
        row_tail = m - c
        after_rows = n - r
        result.append(str(row_tail + after_rows * m + after_rows * (m - 1)))

# CLAUSE: finish_program
    sys.stdout.write("\n".join(result))

if __name__ == "__main__":
    main()
