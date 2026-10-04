import sys


# --- clause: read_input :: () -> list[tuple[int, int, list[int], list[int]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    q = int(data[pos])
    pos += 1
    cases = []
    for _ in range(q):
        n = int(data[pos])
        k = int(data[pos + 1])
        pos += 2
        spots = [int(token) for token in data[pos:pos + k]]
        pos += k
        heats = [int(token) for token in data[pos:pos + k]]
        pos += k
        cases.append((n, k, spots, heats))
    return cases


# --- clause: sweep :: (n: int, k: int, spots: list[int], heats: list[int]) -> list[int] ---
def sweep(n, k, spots, heats):
    huge = 1 << 62
    best = [huge] * (n + 2)
    for i in range(k):
        spot = spots[i]
        if heats[i] < best[spot]:
            best[spot] = heats[i]
    running = huge
    for i in range(1, n + 1):
        if running < huge:
            running += 1
        if best[i] < running:
            running = best[i]
        best[i] = running
    running = huge
    for i in range(n, 0, -1):
        if running < huge:
            running += 1
        if best[i] < running:
            running = best[i]
        best[i] = running
    return best[1:n + 1]


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, k, spots, heats in read_input():
        out.append(" ".join(map(str, sweep(n, k, spots, heats))))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
