# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys
        from math import comb

        n, p = sys.stdin.readline().split()
        n = int(n)
        p = float(p)

        def prob(k):
            total = comb(n, 3)
            good = 0.0
            if k >= 1 and n - k >= 2:
                good += 0.5 * k * comb(n - k, 2)
            if k >= 2 and n - k >= 1:
                good += comb(k, 2) * (n - k)
            if k >= 3:
                good += comb(k, 3)
            return good / total

        lo, hi = 0, n
        eps = 1e-12
        while lo < hi:
            mid = (lo + hi) // 2
            if prob(mid) + eps >= p:
                hi = mid
            else:
                lo = mid + 1

        print(lo)

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
