# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    def main():
        data = sys.stdin.read().strip().split()
        if not data:
            return

        n = int(data[0])
        grid = data[1:1 + n]

        ans = 0
        for i in range(1, n - 1):
            for j in range(1, n - 1):
                if (
                    grid[i][j] == 'X' and
                    grid[i - 1][j - 1] == 'X' and
                    grid[i - 1][j + 1] == 'X' and
                    grid[i + 1][j - 1] == 'X' and
                    grid[i + 1][j + 1] == 'X'
                ):
                    ans += 1

        print(ans)

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
