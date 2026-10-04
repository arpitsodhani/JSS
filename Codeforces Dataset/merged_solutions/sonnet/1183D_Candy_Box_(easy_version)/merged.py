import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    q = data[0]
    pos = 1
    cases = []
    for _ in range(q):
        n = data[pos]
        pos += 1
        cases.append(data[pos:pos + n])
        pos += n
    return cases

# Clause biggest_gift [Confidence: 0.80]
def biggest_gift(a):
    tally = {}
    for value in a:
        tally[value] = tally.get(value, 0) + 1
    sizes = sorted(tally.values(), reverse=True)
    amount = 0
    allowed = len(a) + 1
    for size in sizes:
        take = size if size < allowed - 1 else allowed - 1
        if take <= 0:
            break
        amount += take
        allowed = take
    return amount

# Clause main [Confidence: 1.00]
def main():
    out = []
    for a in read_input():
        out.append(biggest_gift(a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()

