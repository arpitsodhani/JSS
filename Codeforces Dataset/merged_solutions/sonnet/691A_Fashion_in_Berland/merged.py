import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    buttons = list(map(int, data[1:n + 1]))
    return n, buttons

# Clause fastened_well [Confidence: 0.60]
def fastened_well(n, buttons):
    done = 0
    for value in buttons:
        done += value
    if n == 1:
        if done == 1:
            return "YES"
        return "NO"
    if done == n - 1:
        return "YES"
    return "NO"

# Clause main [Confidence: 1.00]
def main():
    n, buttons = read_input()
    sys.stdout.write(fastened_well(n, buttons) + "\n")


if __name__ == "__main__":
    main()

