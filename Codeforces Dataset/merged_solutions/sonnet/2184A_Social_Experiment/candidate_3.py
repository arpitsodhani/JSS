# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def decide(n):
    if n == 1:
        return 1
    return 0 if any(n % d == 0 for d in (2, 3)) else 1

def main():
    text = sys.stdin.buffer.read().strip()
    if text:
        sys.stdout.write(str(decide(int(text.split()[0]))))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
