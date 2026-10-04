# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys
        from collections import Counter

        data = sys.stdin.read().split()
        n = int(data[0])
        k = int(data[1])
        s = data[2]

        print("YES" if max(Counter(s).values(), default=0) <= k else "NO")

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
