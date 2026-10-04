# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        n = int(input())

        if n <= 2:
            print("No")
        else:
            print("Yes")
            if n % 2:
                x = n
            else:
                x = n // 2
            print(1, x)
            rest = [i for i in range(1, n + 1) if i != x]
            print(len(rest), *rest)

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
