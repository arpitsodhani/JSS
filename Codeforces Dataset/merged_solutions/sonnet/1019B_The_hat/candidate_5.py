# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def first_same_across(n, values):
    half = n // 2
    matches = (i + 1 for i in range(half) if values[i] == values[i + half])
    return next(matches, -1)

# CLAUSE: finish_program
def main():
    content = sys.stdin.buffer.read()
    if not content.strip():
        return
    data = list(map(int, content.split()))
    sys.stdout.write(str(first_same_across(data[0], data[1:])))

if __name__ == "__main__":
    main()
