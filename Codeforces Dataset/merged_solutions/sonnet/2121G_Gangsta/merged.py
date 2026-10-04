import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    cases = []
    pos = 1
    for _ in range(t):
        pos += 1
        cases.append(data[pos].decode())
        pos += 1
    return cases

# Clause total_imbalance [Confidence: 0.80]
def total_imbalance(s):
    prefixes = [0]
    balance = 0
    for ch in s:
        balance += 1 if ch == "1" else -1
        prefixes.append(balance)
    prefixes.sort()
    total = 0
    running = 0
    for i in range(len(prefixes)):
        total += prefixes[i] * i - running
        running += prefixes[i]
    return total

# Clause solve_case [Confidence: 1.00]
def solve_case(s):
    n = len(s)
    lengths = n * (n + 1) * (n + 2) // 6
    return (lengths + total_imbalance(s)) // 2

# Clause main [Confidence: 1.00]
def main():
    out = []
    for s in read_input():
        out.append(str(solve_case(s)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

