# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    def solve():
        data = list(map(int, sys.stdin.buffer.read().split()))
        t = data[0]
        idx = 1
        out = []

        for _ in range(t):
            n = data[idx]
            idx += 1
            a = data[idx:idx + n]
            idx += n

            b = [0] * n
            start = 0

            if n % 2 == 1:
                if a[0] + a[1] != 0:
                    b[0] = a[2]
                    b[1] = a[2]
                    b[2] = -(a[0] + a[1])
                else:
                    b[0] = a[1]
                    b[2] = a[1]
                    b[1] = -(a[0] + a[2])
                start = 3

            for i in range(start, n, 2):
                b[i] = a[i + 1]
                b[i + 1] = -a[i]

            out.append(" ".join(map(str, b)))

        sys.stdout.write("\n".join(out))

    if __name__ == "__main__":
        solve()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
