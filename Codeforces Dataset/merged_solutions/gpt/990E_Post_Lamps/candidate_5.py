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

            n, m, k = data[0], data[1], data[2]
            blocked = data[3:3 + m]
            a = data[3 + m:3 + m + k]

            bad = [False] * n
            for x in blocked:
                bad[x] = True

            last = [-1] * n
            p = -1
            for i in range(n):
                if not bad[i]:
                    p = i
                last[i] = p

            ans = 10 ** 30

            for l in range(1, k + 1):
                cur = 0
                cnt = 0
                ok = True

                while cur < n:
                    pos = last[cur]
                    if pos == -1 or pos + l <= cur:
                        ok = False
                        break
                    cnt += 1
                    cur = pos + l

                if ok:
                    ans = min(ans, cnt * a[l - 1])

            print(ans if ans < 10 ** 30 else -1)

        if __name__ == "__main__":
            main()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
