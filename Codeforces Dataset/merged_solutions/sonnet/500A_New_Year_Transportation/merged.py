import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    cells = raw[0]
    goal = raw[1]
    steps = raw[2:cells + 1]
    return cells, goal, steps

# Clause can_reach [Confidence: 1.00]
def can_reach(n, t, jumps):
    cell = 1
    while cell < t:
        cell += jumps[cell - 1]
    return cell == t

# Clause main [Confidence: 1.00]
def main():
    n, t, jumps = read_input()
    answer = "YES" if can_reach(n, t, jumps) else "NO"
    print(answer)


if __name__ == "__main__":
    main()

