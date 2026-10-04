import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    values = [int(token) for token in data[1:n + 1]]
    return n, values


# --- clause: build_basis :: (values: list[int], limit: int) -> list[int] ---
def build_basis(values, limit):
    reduced = []
    picks = []
    for v in values:
        if v >= limit:
            continue
        cur = v
        for b in reduced:
            if cur ^ b < cur:
                cur ^= b
        if cur:
            reduced.append(cur)
            reduced.sort(reverse=True)
            picks.append(v)
    return picks


# --- clause: magical :: (n: int, values: list[int]) -> list[str] ---
def magical(n, values):
    values.sort()
    best = 0
    chosen = []
    for x in range(0, 19):
        picks = build_basis(values, 1 << x)
        if len(picks) == x:
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
    print("\n".join(magical(n, values)))


if __name__ == "__main__":
    main()
