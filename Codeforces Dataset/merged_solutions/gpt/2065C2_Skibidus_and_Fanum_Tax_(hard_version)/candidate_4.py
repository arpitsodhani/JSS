# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys
    from bisect import bisect_left

    def solve():
        data = list(map(int, sys.stdin.buffer.read().split()))
        t = data[0]
        idx = 1
        ans = []

        for _ in range(t):
            n = data[idx]
            m = data[idx + 1]
            idx += 2

            a = data[idx:idx + n]
            idx += n

            b = data[idx:idx + m]
            idx += m
            b.sort()

            prev = -10**30
            ok = True

            for x in a:
                best = 10**30

                if x >= prev:
                    best = x

                pos = bisect_left(b, prev + x)
                if pos < m:
                    y = b[pos] - x
                    if y < best:
                        best = y

                if best == 10**30:
                    ok = False
                    break

                prev = best

            ans.append("YES" if ok else "NO")

        sys.stdout.write("\n".join(ans))

    if __name__ == "__main__":
        solve()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
