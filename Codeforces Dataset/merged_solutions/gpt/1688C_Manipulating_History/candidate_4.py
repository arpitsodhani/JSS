# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    def main():
        data = sys.stdin.read().split()
        tc = int(data[0])
        idx = 1
        ans = []

        for _ in range(tc):
            n = int(data[idx])
            idx += 1
            x = 0
            for _ in range(2 * n + 1):
                for c in data[idx]:
                    x ^= ord(c)
                idx += 1
            ans.append(chr(x))

        print("\n".join(ans))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
