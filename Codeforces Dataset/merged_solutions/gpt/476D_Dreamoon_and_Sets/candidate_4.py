# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    def main():
        k, n = map(int, sys.stdin.readline().split())
        print(k * (6 * n - 1))
        for i in range(n):
            a = 6 * i + 1
            print(k * a, k * (a + 1), k * (a + 2), k * (a + 4))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
