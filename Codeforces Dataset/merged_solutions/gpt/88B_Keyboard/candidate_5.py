# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys
        import math

        def main():
            data = sys.stdin.read().split()
            if not data:
                return

            n = int(data[0])
            m = int(data[1])
            x = int(data[2])

            keyboard = data[3:3 + n]
            q = int(data[3 + n])
            text = data[4 + n]

            positions = [[] for _ in range(26)]
            shifts = []

            for i in range(n):
                row = keyboard[i]
                for j, ch in enumerate(row):
                    if ch == 'S':
                        shifts.append((i, j))
                    else:
                        positions[ord(ch) - 97].append((i, j))

            need_extra = [False] * 26
            x2 = x * x

            if shifts:
                for c in range(26):
                    if positions[c]:
                        ok_close = False
                        for i, j in positions[c]:
                            for si, sj in shifts:
                                if (i - si) * (i - si) + (j - sj) * (j - sj) <= x2:
                                    ok_close = True
                                    break
                            if ok_close:
                                break
                        need_extra[c] = not ok_close

            ans = 0

            for ch in text:
                if ch.islower():
                    if not positions[ord(ch) - 97]:
                        print(-1)
                        return
                else:
                    idx = ord(ch.lower()) - 97
                    if not positions[idx] or not shifts:
                        print(-1)
                        return
                    if need_extra[idx]:
                        ans += 1

            print(ans)

        if __name__ == "__main__":
            main()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
