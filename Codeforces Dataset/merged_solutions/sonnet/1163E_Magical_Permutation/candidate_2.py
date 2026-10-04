import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    values = list(map(int, data[1:n + 1]))
    return n, values


# --- clause: build_basis :: (values: list[int], limit: int) -> list[int] ---
def build_basis(values, limit):
    reduced = [0] * 20
    picks = []
    for v in values:
        if v >= limit:
            continue
        cur = v
        for bit in range(19, -1, -1):
            if not cur >> bit & 1:
                continue
            if reduced[bit] == 0:
                reduced[bit] = cur
                picks.append(v)
                cur = 0
                break
            cur ^= reduced[bit]
    return picks


# --- clause: magical :: (n: int, values: list[int]) -> list[str] ---
def magical(n, values):
    values.sort()
    best = 0
    chosen = []
    for x in range(0, 19):
        picks = build_basis(values, 1 << x)
        if x == len(picks):
            best = x
            chosen = picks
    out = [str(best)]
    row = []
    for i in range(1 << best):
        gray = i ^ (i >> 1)
        value = 0
        for bit in range(best):
            if gray >> bit & 1:
                value ^= chosen[bit]
        row.append(str(value))
    out.append(" ".join(row))
    return out


# --- clause: main :: () -> None ---
def main():
    n, values = read_input()
    sys.stdout.write("%s\n" % "\n".join(magical(n, values)))


if __name__ == "__main__":
    main()
