# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    sticks = sorted(int(x) for x in data[1:n + 1])
    pairs = 0
    index = 0
    while index + 1 < n:
        if sticks[index] == sticks[index + 1]:
            pairs += 1
            index += 2
        else:
            index += 1

# CLAUSE: finish_program
    print(pairs // 2)

if __name__ == "__main__":
    main()
