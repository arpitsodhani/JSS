import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    a = data[2:2 + n]
    pos = 2 + n
    steps = []
    for _ in range(m):
        kind = data[pos]
        if kind == 1:
            steps.append([1, data[pos + 1], data[pos + 2]])
            pos += 3
        else:
            steps.append([kind, data[pos + 1]])
            pos += 2
    return a, steps

# Clause run_steps [Confidence: 1.00]
def run_steps(a, steps):
    shift = 0
    collected = []
    for step in steps:
        if step[0] == 1:
            a[step[1] - 1] = step[2] - shift
        elif step[0] == 2:
            shift += step[1]
        else:
            collected.append(a[step[1] - 1] + shift)
    return collected

# Clause main [Confidence: 1.00]
def main():
    a, steps = read_input()
    sys.stdout.write("\n".join(map(str, run_steps(a, steps))) + "\n")


if __name__ == "__main__":
    main()

