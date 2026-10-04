# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        data = list(map(int, sys.stdin.read().split()))
        n = data[0]
        f = [0] + data[1:1 + n]

        for i in range(1, n + 1):
            if f[f[f[i]]] == i:
                print("YES")
                break
        else:
            print("NO")

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
