# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    def solve():
        data = list(map(int, sys.stdin.buffer.read().split()))
        t = data[0]
        p = 1
        out = []

        for _ in range(t):
            n = data[p]
            p += 1
            a = data[p:p + n]
            p += n
            b = data[p:p + n]
            p += n

            if a[-1] == b[-1]:
                out.append(str(n))
                continue

            seen = [False] * (n + 1)
            ans = -1

            for i in range(n - 2, -1, -1):
                if (
                    a[i] == b[i]
                    or a[i] == a[i + 1]
                    or b[i] == b[i + 1]
                    or seen[a[i]]
                    or seen[b[i]]
                ):
                    ans = i
                    break

                seen[a[i + 1]] = True
                seen[b[i + 1]] = True

            out.append(str(ans + 1))

        sys.stdout.write("\n".join(out))

    if __name__ == "__main__":
        solve()

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
