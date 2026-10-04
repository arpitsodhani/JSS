# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def answer_for(n):
    if n < 2:
        return 1
    last = n * n
    best = last + (last - 1) + (last - n)
    if n > 2:
        inner = 5 * (last - n - 1)
        edge = (last - 1) + (last - 2) + last + (last - n - 1) + (last - n - 1)
        best = max(best, inner, edge)
    return best

def main():
    parts = sys.stdin.buffer.read().split()
    if len(parts) == 0:
        return
    sys.stdout.write(str(answer_for(int(parts[0]))))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
