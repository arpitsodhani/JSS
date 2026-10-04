import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    lights = list(map(int, data[1:n + 1]))
    return n, lights

# Clause count_switches [Confidence: 0.80]
def count_switches(n, lights):
    state = list(lights)
    turned = 0
    for i in range(1, n - 1):
        if state[i - 1] == 1 and state[i] == 0 and state[i + 1] == 1:
            state[i + 1] = 0
            turned += 1
    return turned

# Clause main [Confidence: 1.00]
def main():
    n, lights = read_input()
    sys.stdout.write(str(count_switches(n, lights)) + "\n")


if __name__ == "__main__":
    main()

