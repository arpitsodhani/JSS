import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        x = int(data[pos + 1])
        k = int(data[pos + 2])
        s = data[pos + 3].decode()
        pos += 4
        cases.append((n, x, k, s))
    return cases

# Clause first_zero_time [Confidence: 0.80]
def first_zero_time(start, s):
    pos = start
    for i in range(len(s)):
        pos += 1 if s[i] == "R" else -1
        if pos == 0:
            return i + 1
    return -1

# Clause solve_case [Confidence: 1.00]
def solve_case(n, x, k, s):
    arrival = first_zero_time(x, s)
    if arrival < 0 or arrival > k:
        return 0
    period = first_zero_time(0, s)
    if period < 0:
        return 1
    return 1 + (k - arrival) // period

# Clause main [Confidence: 1.00]
def main():
    out = []
    for n, x, k, s in read_input():
        out.append(str(solve_case(n, x, k, s)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

