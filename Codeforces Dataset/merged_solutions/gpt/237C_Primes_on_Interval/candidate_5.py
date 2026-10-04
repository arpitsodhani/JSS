# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys
        import math

        def main():
            data = list(map(int, sys.stdin.buffer.read().split()))
            if not data:
                return

            a, b, k = data
            is_prime = [True] * (b + 1)
            if b >= 0:
                is_prime[0] = False
            if b >= 1:
                is_prime[1] = False

            for i in range(2, int(math.isqrt(b)) + 1):
                if is_prime[i]:
                    start = i * i
                    is_prime[start:b + 1:i] = [False] * (((b - start) // i) + 1)

            pref = [0] * (b + 1)
            for i in range(1, b + 1):
                pref[i] = pref[i - 1] + (1 if is_prime[i] else 0)

            if pref[b] - pref[a - 1] < k:
                print(-1)
                return

            def ok(length):
                last = b - length + 1
                for x in range(a, last + 1):
                    if pref[x + length - 1] - pref[x - 1] < k:
                        return False
                return True

            lo, hi = 1, b - a + 1
            ans = hi
            while lo <= hi:
                mid = (lo + hi) // 2
                if ok(mid):
                    ans = mid
                    hi = mid - 1
                else:
                    lo = mid + 1

            print(ans)

        if __name__ == "__main__":
            main()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
