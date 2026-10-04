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
        q = data[pos + 2]
        pos += 3
        cases.append((k, q, data[pos:pos + n]))
        pos += n
    return cases

# Clause count_vacations [Confidence: 0.80]
def count_vacations(k, q, a):
    amount = 0
    run = 0
    for value in a + [q + 1]:
        if value <= q:
            run += 1
            continue
        if run >= k:
            spare = run - k + 1
            amount += spare * (spare + 1) // 2
        run = 0
    return amount

# Clause main [Confidence: 1.00]
def main():
    out = []
    for k, q, a in read_input():
        out.append(count_vacations(k, q, a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()

