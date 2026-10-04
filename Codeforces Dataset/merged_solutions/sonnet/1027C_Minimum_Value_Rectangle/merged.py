import sys

# Clause read_input [Confidence: 0.80]
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        sticks = [int(token) for token in data[pos:pos + n]]
        pos += n
        cases.append(sticks)
    return cases

# Clause pair_lengths [Confidence: 1.00]
def pair_lengths(sticks):
    counts = pair_lengths.__dict__.setdefault("_counts", [0] * 10001)
    touched = []
    for value in sticks:
        if counts[value] == 0:
            touched.append(value)
        counts[value] += 1
    touched.sort()
    pool = []
    for value in touched:
        c = counts[value]
        if c >= 2:
            pool.append(value)
            if c >= 4:
                pool.append(value)
        counts[value] = 0
    return pool

# Clause best_rectangle [Confidence: 1.00]
def best_rectangle(pool):
    short = pool[0]
    long = pool[1]
    for i in range(1, len(pool) - 1):
        a = pool[i]
        b = pool[i + 1]
        if b * short < long * a:
            short = a
            long = b
    return short, long

# Clause main [Confidence: 0.60]
def main():
    out = []
    for sticks in read_input():
        pool = pair_lengths(sticks)
        short, long = best_rectangle(pool)
        out.append("%d %d %d %d" % (short, short, long, long))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

