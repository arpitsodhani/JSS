# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        s = input().strip()

        for i in range(len(s) + 1):
            for c in "abcdefghijklmnopqrstuvwxyz":
                t = s[:i] + c + s[i:]
                if t == t[::-1]:
                    print(t)
                    raise SystemExit

        print("NA")

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
