# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    def solve():
        data = list(map(int, sys.stdin.read().split()))
        t = data[0]
        ans = []

        for n in data[1:1 + t]:
            c2 = 0
            c3 = 0

            while n % 2 == 0:
                c2 += 1
                n //= 2

            while n % 3 == 0:
                c3 += 1
                n //= 3

            if n != 1 or c2 > c3:
                ans.append("-1")
            else:
                ans.append(str(2 * c3 - c2))

        sys.stdout.write("\n".join(ans))

    if __name__ == "__main__":
        solve()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
