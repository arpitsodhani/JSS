# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        s = input().strip()
        a = int(s[0])
        op = s[1]
        b = int(s[2])
        print(a + b if op == '+' else a - b)

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
