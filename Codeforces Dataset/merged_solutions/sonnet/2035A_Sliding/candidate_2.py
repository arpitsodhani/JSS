# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    t = values[0]
    ans = []
    p = 1
    for _ in range(t):
        n, m, r, c = values[p], values[p + 1], values[p + 2], values[p + 3]
        p += 4
        ans.append(str(n * m - ((r - 1) * m + c) + (n - r) * (m - 1)))

# CLAUSE: finish_program
    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    main()
