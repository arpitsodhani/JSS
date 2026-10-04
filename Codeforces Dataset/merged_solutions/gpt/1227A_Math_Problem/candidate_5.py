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
            max_l = -10**18
            min_r = 10**18

            for _ in range(n):
                l = data[idx]
                r = data[idx + 1]
                idx += 2
                if l > max_l:
                    max_l = l
                if r < min_r:
                    min_r = r

            ans.append(str(max(0, max_l - min_r)))

        print("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
