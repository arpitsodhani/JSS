# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        n, z = data[0], data[1]
        x = sorted(data[2:])

        i = 0
        j = n // 2
        ans = 0

        while i < n // 2 and j < n:
            if x[j] - x[i] >= z:
                ans += 1
                i += 1
                j += 1
            else:
                j += 1

        print(ans)

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
