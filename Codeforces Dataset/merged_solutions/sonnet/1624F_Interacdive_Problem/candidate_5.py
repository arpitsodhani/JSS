# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        def main():
            data = list(map(int, sys.stdin.read().split()))
            if not data:
                return
    
            n = data[0]
            x = data[1]
            print(x)

        if __name__ == "__main__":
            main()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
