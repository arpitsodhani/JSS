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

# Clause count_gifts [Confidence: 1.00]
def count_gifts(k, gold):
    purse = 0
    gifts = 0
    for entry in gold:
        if entry >= k:
            purse += entry
        elif entry == 0 and purse:
            purse -= 1
            gifts += 1
    return gifts

# Clause main [Confidence: 1.00]
def main():
    out = []
    for k, gold in read_input():
        out.append(count_gifts(k, gold))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()

