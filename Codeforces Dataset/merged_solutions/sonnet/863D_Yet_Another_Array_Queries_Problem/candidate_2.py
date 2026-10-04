import sys


# --- clause: read_input :: () -> tuple[int, int, int, list[int], list[int], list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    q = int(data[1])
    m = int(data[2])
    values = list(map(int, data[3:3 + n]))
    steps = [int(token) for token in data[3 + n:3 + n + 3 * q]]
    wanted = [int(token) for token in data[3 + n + 3 * q:3 + n + 3 * q + m]]
    return n, q, m, values, steps, wanted


# --- clause: trace_back :: (spot: int, q: int, steps: list[int]) -> int ---
def trace_back(spot, q, steps):
    for i in range(q - 1, -1, -1):
        kind = steps[3 * i]
        l = steps[3 * i + 1]
        r = steps[3 * i + 2]
        if not l <= spot <= r:
            continue
        if kind == 1:
            spot = r if spot == l else spot - 1
        else:
            spot = l + r - spot
    return spot


# --- clause: main :: () -> None ---
def main():
    n, q, m, values, steps, wanted = read_input()
    out = []
    for spot in wanted:
        out.append(str(values[trace_back(spot, q, steps) - 1]))
    sys.stdout.write("%s\n" % " ".join(out))


if __name__ == "__main__":
    main()
