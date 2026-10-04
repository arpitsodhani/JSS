# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        data = sys.stdin.read().split(maxsplit=1)
        k = int(data[0])
        s = data[1].rstrip('\r\n')

        parts = []
        last = 0
        for i, ch in enumerate(s):
            if ch == ' ' or ch == '-':
                parts.append(i - last + 1)
                last = i + 1
        parts.append(len(s) - last)

        def ok(w):
            lines = 1
            cur = 0
            for x in parts:
                if x > w:
                    return False
                if cur + x <= w:
                    cur += x
                else:
                    lines += 1
                    cur = x
            return lines <= k

        lo, hi = max(parts), len(s)
        while lo < hi:
            mid = (lo + hi) // 2
            if ok(mid):
                hi = mid
            else:
                lo = mid + 1

        print(lo)

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
