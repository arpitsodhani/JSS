# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    def main():
        data = sys.stdin.buffer.read().split()
        t = int(data[0])
        ans = []
        idx = 1
        for _ in range(t):
            n = int(data[idx])
            k = int(data[idx + 1])
            idx += 2
            ans.append(str(k + (k - 1) // (n - 1)))
        sys.stdout.write("\n".join(ans))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
