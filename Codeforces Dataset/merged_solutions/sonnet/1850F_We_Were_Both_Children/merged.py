import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        cases.append(data[pos:pos + n])
        pos += n
    return cases

# Clause best_trap [Confidence: 1.00]
def best_trap(hops):
    n = len(hops)
    seen = [0] * (n + 1)
    for value in hops:
        if value <= n:
            seen[value] += 1
    caught = [0] * (n + 1)
    for value in range(1, n + 1):
        if not seen[value]:
            continue
        spot = value
        while spot <= n:
            caught[spot] += seen[value]
            spot += value
    best = 0
    for spot in range(1, n + 1):
        if caught[spot] > best:
            best = caught[spot]
    return best

# Clause main [Confidence: 1.00]
def main():
    out = []
    for hops in read_input():
        out.append(best_trap(hops))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()

