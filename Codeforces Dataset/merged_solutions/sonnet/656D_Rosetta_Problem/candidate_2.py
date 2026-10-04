# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = sys.stdin.read().strip()
    answer = data.count("1")

# CLAUSE: finish_program
    print(answer)

if __name__ == "__main__":
    main()
