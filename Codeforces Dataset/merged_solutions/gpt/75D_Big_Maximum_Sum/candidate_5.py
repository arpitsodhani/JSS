# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        def main():
            data = list(map(int, sys.stdin.buffer.read().split()))
            if not data:
                return

            p = 0
            n = data[p]
            m = data[p + 1]
            p += 2

            sums = [0] * n
            prefs = [0] * n
            suffs = [0] * n
            bests = [0] * n

            for i in range(n):
                k = data[p]
                p += 1
                arr = data[p:p + k]
                p += k

                total = 0
                pref = -10**30
                cur = 0
                best = -10**30

                for x in arr:
                    total += x
                    pref = max(pref, total)
                    cur = max(x, cur + x)
                    best = max(best, cur)

                suffix_sum = 0
                suff = -10**30
                for x in reversed(arr):
                    suffix_sum += x
                    suff = max(suff, suffix_sum)

                sums[i] = total
                prefs[i] = pref
                suffs[i] = suff
                bests[i] = best

            order = data[p:p + m]

            ans = -10**30
            tail = -10**30

            for idx in order:
                idx -= 1
                ans = max(ans, bests[idx])
                if tail != -10**30:
                    ans = max(ans, tail + prefs[idx])
                    tail = max(suffs[idx], tail + sums[idx])
                else:
                    tail = suffs[idx]

            print(ans)

        if __name__ == "__main__":
            main()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
