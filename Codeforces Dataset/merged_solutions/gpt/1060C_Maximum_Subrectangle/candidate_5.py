# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        def min_sums(arr):
            n = len(arr)
            pref = [0] * (n + 1)
            for i, v in enumerate(arr):
                pref[i + 1] = pref[i] + v

            inf = 10**30
            res = [inf] * (n + 1)
            for l in range(1, n + 1):
                best = inf
                for i in range(n - l + 1):
                    s = pref[i + l] - pref[i]
                    if s < best:
                        best = s
                res[l] = best
            return res

        def main():
            data = list(map(int, sys.stdin.read().split()))
            if not data:
                return

            n, m = data[0], data[1]
            a = data[2:2 + n]
            b = data[2 + n:2 + n + m]
            x = data[2 + n + m]

            ma = min_sums(a)
            mb = min_sums(b)

            ans = 0
            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    if ma[i] * mb[j] <= x:
                        area = i * j
                        if area > ans:
                            ans = area

            print(ans)

        if __name__ == "__main__":
            main()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
