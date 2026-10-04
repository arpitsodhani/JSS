# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        data = list(map(int, sys.stdin.buffer.read().split()))
        t = data[0]
        idx = 1
        ans = []

        for _ in range(t):
            n = data[idx]
            idx += 1
            freq = [0] * (n + 1)

            for _ in range(n):
                a = data[idx]
                idx += 1
                if a <= n:
                    freq[a] += 1

            caught = [0] * (n + 1)
            best = 0

            for hop in range(1, n + 1):
                if freq[hop]:
                    for pos in range(hop, n + 1, hop):
                        caught[pos] += freq[hop]
                        if caught[pos] > best:
                            best = caught[pos]

            ans.append(str(best))

        sys.stdout.write("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
