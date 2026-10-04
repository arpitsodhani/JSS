# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    n = values[0]
    weights = values[1:n + 1]
    limit = 150002
    freq = [0] * (limit + 2)
    for weight in weights:
        freq[weight] += 1
    used = [False] * (limit + 3)
    answer = 0
    for weight in range(1, limit + 1):
        while freq[weight]:
            if weight > 1 and not used[weight - 1]:
                used[weight - 1] = True
                answer += 1
            elif not used[weight]:
                used[weight] = True
                answer += 1
            elif not used[weight + 1]:
                used[weight + 1] = True
                answer += 1
            freq[weight] -= 1
    sys.stdout.write(str(answer))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
