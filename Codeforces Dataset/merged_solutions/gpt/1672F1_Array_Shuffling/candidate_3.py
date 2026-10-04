# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys
    from collections import Counter

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        t = data[0]
        p = 1
        out = []
        for _ in range(t):
            n = data[p]
            p += 1
            a = data[p:p + n]
            p += n

            m = max(Counter(a).values())
            items = sorted((a[i], i) for i in range(n))
            b = [0] * n

            for i in range(n):
                b[items[i][1]] = items[(i + m) % n][0]

            out.append(" ".join(map(str, b)))

        sys.stdout.write("\n".join(out))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
