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
            k = data[idx + 1]
            idx += 2
            a = data[idx:idx + n]
            idx += n

            seen = [False] * (n + 1)
            for x in a:
                seen[x] = True

            mex = 0
            while seen[mex]:
                mex += 1

            b = [mex] + a
            shift = k % (n + 1)
            rotated = b[-shift:] + b[:-shift] if shift else b
            out.append(" ".join(map(str, rotated[1:])))

        sys.stdout.write("\n".join(out))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
