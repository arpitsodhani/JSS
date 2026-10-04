# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    def bob_score(values, a, b):
        return sum(abs(x - b) < abs(x - a) for x in values)

    def solve():
        data = list(map(int, sys.stdin.buffer.read().split()))
        if not data:
            return

        t = data[0]
        idx = 1
        ans = []

        for _ in range(t):
            n = data[idx]
            a = data[idx + 1]
            idx += 2
            v = data[idx:idx + n]
            idx += n

            candidates = {1, 10**9}
            for x in v:
                candidates.add(x)
                candidates.add(x - 1)
                candidates.add(x + 1)
                candidates.add(2 * x - a - 1)
                candidates.add(2 * x - a)
                candidates.add(2 * x - a + 1)

            best_b = 1
            best = -1
            for b in candidates:
                if 1 <= b <= 10**9:
                    cur = bob_score(v, a, b)
                    if cur > best:
                        best = cur
                        best_b = b

            ans.append(str(best_b))

        sys.stdout.write("\n".join(ans))

    if __name__ == "__main__":
        solve()

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
