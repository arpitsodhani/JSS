import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        k = data[pos + 1]
        pos += 2
        cases.append((k, data[pos:pos + n]))
        pos += n
    return cases

# Clause least_power [Confidence: 1.00]
def least_power(k, a):
    gaps = []
    for i in range(1, len(a)):
        step = a[i] - a[i - 1]
        gaps.append(step if step > 0 else -step)
    gaps.sort(reverse=True)
    amount = 0
    for spot in range(k - 1, len(gaps)):
        amount += gaps[spot]
    return amount

# Clause main [Confidence: 1.00]
def main():
    out = []
    for k, a in read_input():
        out.append(least_power(k, a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()

