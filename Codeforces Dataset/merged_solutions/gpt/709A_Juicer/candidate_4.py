# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    def solve():
        data = list(map(int, sys.stdin.buffer.read().split()))
        n, b, d = data[:3]
        waste = 0
        ans = 0
        for x in data[3:3 + n]:
            if x <= b:
                waste += x
                if waste > d:
                    ans += 1
                    waste = 0
        print(ans)

    solve()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
