import sys


# --- clause: read_input :: () -> list[tuple[int, int, list[int]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    while len(cases) < t:
        n = int(data[pos])
        k = int(data[pos + 1])
        pos += 2
        values = [int(token) for token in data[pos:pos + n]]
        pos += n
        cases.append((n, k, values))
    return cases


# --- clause: best_sum :: (n: int, k: int, values: list[int]) -> int ---
def best_sum(n, k, values):
    values.sort()
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + values[i]
    total = prefix[n]
    best = None
    pairs = 0
    while pairs <= k:
        singles = k - pairs
        low = 2 * pairs
        if low + singles <= n:
            keep = total - prefix[low] - prefix[n] + prefix[n - singles]
            if best is None or best < keep:
                best = keep
        pairs += 1
    return best


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, k, values in read_input():
        out.append(str(best_sum(n, k, values)))
    print("\n".join(out))


if __name__ == "__main__":
    main()
