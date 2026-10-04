import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    idx = 1
    t = int(data[0])
    cases = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        sticks = list(map(int, data[idx:idx + n]))
        idx += n
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
        if b * short < long * a:
            short = a
            long = b
    return short, long


# --- clause: main :: () -> None ---
def main():
    out = []
    for sticks in read_input():
        short, long = best_rectangle(pair_lengths(sticks))
        out.append(" ".join((str(short), str(short), str(long), str(long))))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
