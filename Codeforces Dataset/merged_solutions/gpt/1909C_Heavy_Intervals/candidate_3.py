# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys
    import bisect

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        it = iter(data)
        t = next(it)
        ans = []

        for _ in range(t):
            n = next(it)
            l = [next(it) for _ in range(n)]
            r = [next(it) for _ in range(n)]
            c = [next(it) for _ in range(n)]

            l.sort()
            r.sort()

            available = l[:]
            lengths = []

            for x in r:
                idx = bisect.bisect_left(available, x) - 1
                y = available.pop(idx)
                lengths.append(x - y)

            lengths.sort()
            c.sort(reverse=True)

            ans.append(str(sum(a * b for a, b in zip(lengths, c))))

        sys.stdout.write("\n".join(ans))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
