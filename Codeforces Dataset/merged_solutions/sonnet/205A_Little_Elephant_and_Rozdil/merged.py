import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    times = [int(token) for token in data[1:n + 1]]
    return n, times

# Clause pick_town [Confidence: 0.80]
def pick_town(n, times):
    best = times[0]
    spot = 0
    count = 1
    for i in range(1, n):
        if times[i] < best:
            best = times[i]
            spot = i
            count = 1
        elif times[i] == best:
            count += 1
    if count > 1:
        return "Still Rozdil"
    return str(spot + 1)

# Clause main [Confidence: 1.00]
def main():
    n, times = read_input()
    sys.stdout.write(pick_town(n, times) + "\n")


if __name__ == "__main__":
    main()

