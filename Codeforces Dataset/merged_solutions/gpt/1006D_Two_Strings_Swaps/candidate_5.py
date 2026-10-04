# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        data = sys.stdin.read().split()
        n = int(data[0])
        a = data[1].strip()
        b = data[2].strip()

        ans = 0

        for i in range(n // 2):
            j = n - 1 - i
            chars = [a[i], a[j], b[i], b[j]]
            best = 2

            for c1 in range(26):
                x = chr(97 + c1)
                cost1 = (x != a[i])
                for c2 in range(26):
                    y = chr(97 + c2)
                    cost = cost1 + (y != a[j])
                    if cost >= best:
                        continue
                    cnt = {}
                    for ch in (x, y, b[i], b[j]):
                        cnt[ch] = cnt.get(ch, 0) + 1
                    if all(v % 2 == 0 for v in cnt.values()):
                        best = cost

            ans += best

        if n % 2 == 1 and a[n // 2] != b[n // 2]:
            ans += 1

        print(ans)

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
