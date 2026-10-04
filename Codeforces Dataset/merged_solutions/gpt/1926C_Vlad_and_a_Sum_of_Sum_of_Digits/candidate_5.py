# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        data = list(map(int, sys.stdin.buffer.read().split()))
        t = data[0]
        queries = data[1:]

        m = max(queries)
        pref = [0] * (m + 1)

        for i in range(1, m + 1):
            pref[i] = pref[i // 10] + i % 10

        for i in range(1, m + 1):
            pref[i] += pref[i - 1]

        print("\n".join(str(pref[n]) for n in queries[:t]))

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
