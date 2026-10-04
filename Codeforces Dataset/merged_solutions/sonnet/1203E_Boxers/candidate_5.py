# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    raw = sys.stdin.buffer.read().split()
    n = int(raw[0])
    weights = sorted(int(x) for x in raw[1:n + 1])
    taken = bytearray(150004)
    answer = 0
    for weight in weights:
        left = weight - 1
        if left > 0 and taken[left] == 0:
            taken[left] = 1
            answer += 1
            continue
        if taken[weight] == 0:
            taken[weight] = 1
            answer += 1
            continue
        right = weight + 1
        if taken[right] == 0:
            taken[right] = 1
            answer += 1
    print(answer)

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
