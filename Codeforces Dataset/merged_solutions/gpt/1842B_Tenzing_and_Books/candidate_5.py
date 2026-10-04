# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        data = list(map(int, sys.stdin.buffer.read().split()))
        t = data[0]
        p = 1
        ans = []

        for _ in range(t):
            n = data[p]
            x = data[p + 1]
            p += 2

            stacks = []
            for _ in range(3):
                stacks.append(data[p:p + n])
                p += n

            cur = 0
            for stack in stacks:
                for v in stack:
                    if v | x != x:
                        break
                    cur |= v

            ans.append("Yes" if cur == x else "No")

        print("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
