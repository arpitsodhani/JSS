import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [data[2 + 2 * i].decode() for i in range(t)]

# Clause least_cost [Confidence: 0.80]
def least_cost(s):
    longest = 1
    run = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            run += 1
        else:
            run = 1
        if run > longest:
            longest = run
    return longest + 1

# Clause main [Confidence: 1.00]
def main():
    collected = []
    for s in read_input():
        collected.append(least_cost(s))
    sys.stdout.write("\n".join(map(str, collected)) + "\n")


if __name__ == "__main__":
    main()

