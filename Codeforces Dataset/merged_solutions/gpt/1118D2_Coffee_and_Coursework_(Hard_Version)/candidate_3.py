# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    def main():
        input = sys.stdin.readline
        n, m = map(int, input().split())
        a = sorted(map(int, input().split()), reverse=True)

        if sum(a) < m:
            print(-1)
            return

        def ok(days):
            total = 0
            for i, x in enumerate(a):
                total += max(0, x - i // days)
                if total >= m:
                    return True
            return False

        l, r = 1, n
        ans = n
        while l <= r:
            mid = (l + r) // 2
            if ok(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        print(ans)

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
