# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        data = list(map(int, sys.stdin.buffer.read().split()))
        if not data:
            sys.exit()

        n, c = data[0], data[1]
        idx = 2

        events = {}
        possible = True

        prev_len = data[idx]
        idx += 1
        prev = data[idx:idx + prev_len]
        idx += prev_len

        def forbid(l, r):
            if l > r:
                return
            events[l] = events.get(l, 0) + 1
            if r + 1 <= c:
                events[r + 1] = events.get(r + 1, 0) - 1

        for _ in range(1, n):
            cur_len = data[idx]
            idx += 1
            cur = data[idx:idx + cur_len]
            idx += cur_len

            m = min(len(prev), len(cur))
            p = 0
            while p < m and prev[p] == cur[p]:
                p += 1

            if p == m:
                if len(prev) > len(cur):
                    possible = False
                    break
            else:
                x, y = prev[p], cur[p]
                if x < y:
                    forbid(c - y + 1, c - x)
                else:
                    forbid(0, c - x)
                    forbid(c - y + 1, c - 1)

            prev = cur

        if not possible:
            print(-1)
        else:
            cur_bad = 0
            pos = 0
            answer = -1

            for p in sorted(events):
                if pos < p and cur_bad == 0:
                    answer = pos
                    break
                cur_bad += events[p]
                pos = p

            if answer == -1 and pos < c and cur_bad == 0:
                answer = pos

            print(answer)

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
