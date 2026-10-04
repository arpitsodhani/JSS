# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys
        from bisect import bisect_left

        def main():
            data = list(map(int, sys.stdin.buffer.read().split()))
            n = data[0]
            a = data[1:1 + n]
            a.sort()
            total = sum(a)

            m_idx = 1 + n
            m = data[m_idx]
            idx = m_idx + 1

            ans = []
            for _ in range(m):
                x = data[idx]
                y = data[idx + 1]
                idx += 2

                pos = bisect_left(a, x)
                best = 10**30

                if pos < n:
                    hero = a[pos]
                    best = min(best, max(0, y - (total - hero)))

                if pos > 0:
                    hero = a[pos - 1]
                    best = min(best, x - hero + max(0, y - (total - hero)))

                ans.append(str(best))

            sys.stdout.write("\n".join(ans))

        if __name__ == "__main__":
            main()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
