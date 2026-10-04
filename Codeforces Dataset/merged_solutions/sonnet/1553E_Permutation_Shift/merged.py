import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        m = data[pos + 1]
        pos += 2
        cases.append((m, data[pos:pos + n]))
        pos += n
    return cases

# Clause shift_matches [Confidence: 1.00]
def shift_matches(p):
    n = len(p)
    matches = [0] * n
    for i in range(n):
        matches[(i - p[i] + 1) % n] += 1
    return matches

# Clause swaps_needed [Confidence: 1.00]
def swaps_needed(p, shift):
    n = len(p)
    marked = [False] * n
    moved = 0
    cycles = 0
    for i in range(n):
        if marked[i] or p[i] == (i - shift) % n + 1:
            continue
        cycles += 1
        j = i
        while not marked[j]:
            marked[j] = True
            moved += 1
            j = (p[j] - 1 + shift) % n
    return moved - cycles

# Clause possible_shifts [Confidence: 1.00]
def possible_shifts(m, p):
    n = len(p)
    matches = shift_matches(p)
    found = []
    for shift in range(n):
        if matches[shift] < n - 2 * m:
            continue
        if swaps_needed(p, shift) <= m:
            found.append(shift)
    return found

# Clause main [Confidence: 1.00]
def main():
    out = []
    for m, p in read_input():
        found = possible_shifts(m, p)
        out.append(" ".join(map(str, [len(found)] + found)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

