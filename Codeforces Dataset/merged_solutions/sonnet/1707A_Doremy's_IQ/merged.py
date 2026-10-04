import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        q = data[pos + 1]
        pos += 2
        cases.append((q, data[pos:pos + n]))
        pos += n
    return cases

# Clause choose_contests [Confidence: 1.00]
def choose_contests(q, a):
    n = len(a)
    picks = ["0"] * n
    spent = 0
    for i in range(n - 1, -1, -1):
        if a[i] <= spent:
            picks[i] = "1"
        elif spent < q:
            spent += 1
            picks[i] = "1"
    return "".join(picks)

# Clause main [Confidence: 1.00]
def main():
    collected = []
    for q, a in read_input():
        collected.append(choose_contests(q, a))
    sys.stdout.write("\n".join(collected) + "\n")


if __name__ == "__main__":
    main()

