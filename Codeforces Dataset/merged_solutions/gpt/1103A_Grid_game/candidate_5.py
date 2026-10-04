# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        s = input().strip()

        v = 0
        h = 0

        for c in s:
            if c == '0':
                if v == 0:
                    print(1, 1)
                else:
                    print(3, 1)
                v ^= 1
            else:
                if h == 0:
                    print(1, 3)
                else:
                    print(3, 3)
                h ^= 1

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
