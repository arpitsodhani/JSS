import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        sticks = [int(data[pos + i]) for i in range(n)]
        pos += n
        cases.append(sticks)
    return cases


# --- clause: pair_lengths :: (sticks: list[int]) -> list[int] ---
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


# --- clause: best_rectangle :: (pool: list[int]) -> tuple[int, int] ---
def best_rectangle(pool):
    short = pool[0]
    long = pool[1]
    for i in range(1, len(pool) - 1):
        a = pool[i]
        b = pool[i + 1]
        if long * a > b * short:
            short = a
            long = b
    return short, long


# --- clause: main :: () -> None ---
def main():
    out = []
    for sticks in read_input():
        pool = pair_lengths(sticks)
        short, long = best_rectangle(pool)
        out.append("%d %d %d %d" % (short, short, long, long))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
