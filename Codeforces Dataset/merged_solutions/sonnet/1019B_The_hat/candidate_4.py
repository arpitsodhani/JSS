# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    raw = sys.stdin.buffer.read().split()
    if len(raw) == 0:
        return
    n = int(raw[0])
    values = tuple(int(item) for item in raw[1:])
    half = n // 2
    index = 0
    answer = -1
    while index < half and answer == -1:
        if values[index] == values[index + half]:
            answer = index + 1
        index += 1

# CLAUSE: finish_program
    print(answer)

if __name__ == "__main__":
    main()
