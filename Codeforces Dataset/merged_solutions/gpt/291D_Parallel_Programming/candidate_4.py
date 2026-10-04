# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    def main():
        data = sys.stdin.readline().split()
        if not data:
            return
        n, k = map(int, data)

        need = n - 1
        steps = 0
        p = 1
        while p < need:
            p <<= 1
            steps += 1

        out = []
        noop = " ".join([str(n)] * n)

        for _ in range(k - steps):
            out.append(noop)

        p = 1
        for _ in range(steps):
            row = []
            for i in range(1, n + 1):
                d = n - i
                old = p if d > p else d
                new = 2 * p if d > 2 * p else d
                add = new - old
                row.append(str(n - add))
            out.append(" ".join(row))
            p <<= 1

        sys.stdout.write("\n".join(out))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
