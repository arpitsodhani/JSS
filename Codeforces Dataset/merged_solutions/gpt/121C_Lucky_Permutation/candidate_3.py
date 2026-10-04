# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys
    import math

    def gen_lucky(limit):
        res = []
        def dfs(x):
            if x > limit:
                return
            if x > 0:
                res.append(x)
            dfs(x * 10 + 4)
            dfs(x * 10 + 7)
        dfs(0)
        return sorted(res)

    def main():
        data = sys.stdin.read().split()
        if not data:
            return
        n = int(data[0])
        k = int(data[1])

        fact = [1]
        while fact[-1] < k:
            fact.append(fact[-1] * len(fact))

        m = len(fact) - 1
        if m > n:
            print(-1)
            return

        lucky = gen_lucky(n)
        ans = 0
        suffix_start = n - m + 1

        for x in lucky:
            if x < suffix_start:
                ans += 1

        nums = list(range(suffix_start, n + 1))
        k -= 1

        for pos in range(suffix_start, n + 1):
            r = n - pos
            f = math.factorial(r)
            idx = k // f if f else 0
            k %= f if f else 1
            val = nums.pop(idx)
            if (pos in lucky) and (val in lucky):
                ans += 1

        print(ans)

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
