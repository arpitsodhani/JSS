# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        data = list(map(int, sys.stdin.buffer.read().split()))
        n, l, r = data[0], data[1], data[2]
        a = data[3:3 + n]
        b = data[3 + n:3 + 2 * n]

        l -= 1
        r -= 1

        ok = True

        for i in range(n):
            if (i < l or i > r) and a[i] != b[i]:
                ok = False
                break

        if ok:
            cnt = [0] * (n + 1)
            for x in a[l:r + 1]:
                cnt[x] += 1
            for x in b[l:r + 1]:
                cnt[x] -= 1
            ok = all(x == 0 for x in cnt)

        print("TRUTH" if ok else "LIE")

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
