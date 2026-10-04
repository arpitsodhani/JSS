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
        heats = [int(data[pos + i]) for i in range(k)]
        pos += k
        cases.append((n, k, spots, heats))
    return cases


# --- clause: sweep :: (n: int, k: int, spots: list[int], heats: list[int]) -> list[int] ---
def sweep(n, k, spots, heats):
    best = [1 << 62] * (n + 2)
    huge = 1 << 62
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
    for case in read_input():
        out.append(" ".join(map(str, sweep(case[0], case[1], case[2], case[3]))))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
