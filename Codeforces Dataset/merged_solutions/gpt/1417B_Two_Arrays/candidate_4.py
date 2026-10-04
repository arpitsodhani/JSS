# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        t = data[0]
        idx = 1
        out = []

        for _ in range(t):
            n = data[idx]
            T = data[idx + 1]
            idx += 2
            a = data[idx:idx + n]
            idx += n

            ans = []
            mid_count = 0

            for x in a:
                if 2 * x < T:
                    ans.append(0)
                elif 2 * x > T:
                    ans.append(1)
                else:
                    ans.append(mid_count & 1)
                    mid_count += 1

            out.append(" ".join(map(str, ans)))

        sys.stdout.write("\n".join(out))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
