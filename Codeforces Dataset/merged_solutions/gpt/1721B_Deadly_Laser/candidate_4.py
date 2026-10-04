# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    data = list(map(int, sys.stdin.read().split()))
    if not data:
        sys.exit()

    if (len(data) - 1) % 5 == 0 and data[0] == (len(data) - 1) // 5:
        tests = data[1:]
    else:
        tests = data

    ans = []
    for i in range(0, len(tests), 5):
        n, m, sx, sy, d = tests[i:i + 5]

        impossible = (
            (sx - d <= 1 and sy - d <= 1) or
            (sx + d >= n and sy + d >= m) or
            (sx - d <= 1 and sx + d >= n) or
            (sy - d <= 1 and sy + d >= m)
        )

        ans.append("-1" if impossible else str(n + m - 2))

    print("\n".join(ans))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
