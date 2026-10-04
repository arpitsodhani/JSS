import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    k = data[1]
    return n, k, data[2:2 + n]

# Clause fewest_moves [Confidence: 0.80]
def fewest_moves(n, k, a):
    limit = max(a) + 1
    seen = [0] * limit
    cost = [0] * limit
    best = -1
    for value in sorted(a):
        current = value
        steps = 0
        while True:
            if seen[current] < k:
                seen[current] += 1
                cost[current] += steps
                if seen[current] == k and (best < 0 or cost[current] < best):
                    best = cost[current]
            if current == 0:
                break
            current //= 2
            steps += 1
    return best

# Clause main [Confidence: 1.00]
def main():
    n, k, a = read_input()
    sys.stdout.write(str(fewest_moves(n, k, a)) + "\n")


if __name__ == "__main__":
    main()

