# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    def solve():
        data = list(map(int, sys.stdin.buffer.read().split()))
        t = data[0]
        idx = 1
        out = []

        for _ in range(t):
            n = data[idx]
            k = data[idx + 1]
            idx += 2

            a0 = data[idx:idx + n]
            idx += n
            b0 = data[idx:idx + n]
            idx += n

            pairs = sorted(zip(a0, b0))
            a = [x for x, _ in pairs]
            b = [y for _, y in pairs]

            ans = 0

            marked = -1
            for i in range(n):
                if b[i] == 1:
                    marked = i

            if marked != -1:
                if marked < n // 2:
                    med = a[n // 2]
                else:
                    med = a[n // 2 - 1]
                ans = max(ans, a[marked] + k + med)

            fixed = -1
            for i in range(n):
                if b[i] == 0:
                    fixed = i

            if fixed != -1:
                need = (n + 1) // 2

                def can(x):
                    cnt = 0
                    cost = 0
                    for j in range(n - 1, -1, -1):
                        if j == fixed:
                            continue
                        if a[j] >= x:
                            cnt += 1
                        elif b[j] == 1 and cnt < need:
                            cost += x - a[j]
                            if cost > k:
                                return False
                            cnt += 1
                        if cnt >= need:
                            return True
                    return False

                lo = 0
                hi = max(a) + k + 2
                while lo + 1 < hi:
                    mid = (lo + hi) // 2
                    if can(mid):
                        lo = mid
                    else:
                        hi = mid

                ans = max(ans, a[fixed] + lo)

            out.append(str(ans))

        sys.stdout.write("\n".join(out))

    if __name__ == "__main__":
        solve()

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
