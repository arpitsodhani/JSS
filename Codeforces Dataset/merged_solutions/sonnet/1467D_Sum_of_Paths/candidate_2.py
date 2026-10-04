import sys

MOD = 1000000007


# --- clause: read_input :: () -> tuple[int, int, int, list[int], list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    k = int(data[1])
    q = int(data[2])
    values = list(map(int, data[3:3 + n]))
    updates = [int(token) for token in data[3 + n:3 + n + 2 * q]]
    return n, k, q, values, updates


# --- clause: visit_counts :: (n: int, k: int) -> list[int] ---
def visit_counts(n, k):
    from array import array

    prev = [1] * n
    rows = [array("i", prev)]
    for _ in range(k):
        middle = [(a + b) % MOD for a, b in zip(prev, prev[2:])]
        cur = [prev[1]] + middle + [prev[-2]]
        rows.append(array("i", cur))
        prev = cur

    counts = [0] * n
    for step in range(k + 1):
        first = rows[step]
        second = rows[k - step]
        counts = [(c + a * b) % MOD for c, a, b in zip(counts, first, second)]
    return counts


# --- clause: run_updates :: (n: int, q: int, values: list[int], updates: list[int], counts: list[int]) -> list[str] ---
def run_updates(n, q, values, updates, counts):
    total = 0
    for i in range(n):
        total = (total + counts[i] * values[i]) % MOD
    out = []
    for step in range(q):
        pos = updates[2 * step] - 1
        fresh = updates[2 * step + 1]
        total = (total + counts[pos] * (fresh - values[pos])) % MOD
        values[pos] = fresh
        out.append(str(total % MOD))
    return out


# --- clause: main :: () -> None ---
def main():
    n, k, q, values, updates = read_input()
    counts = visit_counts(n, k)
    sys.stdout.write("%s\n" % "\n".join(run_updates(n, q, values, updates, counts)))


if __name__ == "__main__":
    main()
