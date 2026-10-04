# Clause setup_environment [Confidence: 1.00]
import sys


# Clause solve_logic [Confidence: 0.60]
def solve(n, k):
    if n == 1:
        return "\n".join("1" for _ in range(k))
    last = n - 1
    minimum = 0
    power = 1
    while power < last:
        power <<= 1
        minimum += 1
    if k < minimum:
        return "-1"
    answer = []
    left = 1
    for _ in range(k):
        right = left << 1
        if right > last:
            right = last
        line = [str(n)] * n
        for distance in range(left + 1, right + 1):
            cell = n - distance
            line[cell - 1] = str(n - (distance - left))
        answer.append(" ".join(line))
        left = right
    return "\n".join(answer)


# Clause finish_program [Confidence: 0.60]
def main():
    data = sys.stdin.read().split()
    if data:
        sys.stdout.write(solve(int(data[0]), int(data[1])))

if __name__ == "__main__":
    main()


