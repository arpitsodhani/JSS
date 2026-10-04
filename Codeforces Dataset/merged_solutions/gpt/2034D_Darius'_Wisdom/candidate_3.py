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
            a = [0] + data[p:p + n]
            p += n

            ans = []
            l = 1
            r = n

            while l <= n and a[l] == 0:
                l += 1
            while r >= 1 and a[r] == 2:
                r -= 1

            i = 1
            while i <= r:
                if a[i] == 2:
                    while a[r] == 2:
                        r -= 1
                    ans.append((i, r))
                    a[i], a[r] = a[r], a[i]
                    r -= 1
                i += 1

            i = n
            while i >= l:
                if a[i] == 0:
                    while a[l] == 0:
                        l += 1
                    ans.append((l, i))
                    a[l], a[i] = a[i], a[l]
                    l += 1
                i -= 1

            out.append(str(len(ans)))
            out.extend(f"{u} {v}" for u, v in ans)

        sys.stdout.write("\n".join(out))

    if __name__ == "__main__":
        solve()

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
