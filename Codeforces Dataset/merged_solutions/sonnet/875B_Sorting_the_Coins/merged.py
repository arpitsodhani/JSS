import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]

# Clause hardness_steps [Confidence: 1.00]
def hardness_steps(order):
    n = len(order)
    placed = [False] * (n + 2)
    tail = n
    collected = [1]
    for i in range(n):
        placed[order[i]] = True
        while tail >= 1 and placed[tail]:
            tail -= 1
        collected.append(i + 1 - (n - tail) + 1)
    return collected

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write(" ".join(map(str, hardness_steps(read_input()))) + "\n")


if __name__ == "__main__":
    main()

