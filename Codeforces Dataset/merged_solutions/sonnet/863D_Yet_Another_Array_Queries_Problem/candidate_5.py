import sys


# --- clause: read_input :: () -> tuple[int, int, int, list[int], list[int], list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    q = int(data[1])
    m = int(data[2])
    values = [int(token) for token in data[3:3 + n]]
    steps = [int(token) for token in data[3 + n:3 + n + 3 * q]]
    tail = 3 + n + 3 * q
    wanted = list(map(int, data[tail:tail + m]))
    return n, q, m, values, steps, wanted


# --- clause: trace_back :: (spot: int, q: int, steps: list[int]) -> int ---
def trace_back(spot, q, steps):
    for i in range(q - 1, -1, -1):
        kind = steps[3 * i]
        l = steps[3 * i + 1]
        r = steps[3 * i + 2]
        if spot < l or spot > r:
            continue
        if kind == 2:
            spot = l + r - spot
        elif l == spot:
            spot = r
        else:
            spot = spot - 1
    return spot


# --- clause: main :: () -> None ---
def main():
    n, q, m, values, steps, wanted = read_input()
    out = []
    for spot in wanted:
        out.append(str(values[trace_back(spot, q, steps) - 1]))
    sys.stdout.write(" ".join(out) + "\n")


if __name__ == "__main__":
    main()
