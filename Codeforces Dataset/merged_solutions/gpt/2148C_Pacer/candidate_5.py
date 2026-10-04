# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        data = list(map(int, sys.stdin.read().split()))
        t = data[0]
        idx = 1
        ans = []

        for _ in range(t):
            n = data[idx]
            m = data[idx + 1]
            idx += 2

            time = 0
            side = 0
            score = 0

            for _ in range(n):
                a = data[idx]
                b = data[idx + 1]
                idx += 2

                d = a - time
                need = side ^ b

                if d % 2 == need:
                    score += d
                else:
                    score += d - 1

                time = a
                side = b

            score += m - time
            ans.append(str(score))

        print("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
