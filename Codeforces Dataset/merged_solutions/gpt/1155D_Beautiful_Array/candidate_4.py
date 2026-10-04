# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        n, x = data[0], data[1]
        a = data[2:]

        dp0 = dp1 = dp2 = 0
        ans = 0

        for v in a:
            old0, old1, old2 = dp0, dp1, dp2
            dp0 = max(0, old0 + v)
            dp1 = max(0, old0 + v * x, old1 + v * x)
            dp2 = max(0, old1 + v, old2 + v)
            ans = max(ans, dp0, dp1, dp2)

        print(ans)

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
