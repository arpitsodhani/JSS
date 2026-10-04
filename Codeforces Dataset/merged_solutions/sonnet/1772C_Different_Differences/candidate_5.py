import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    cases = []
    for i in range(t):
        cases.append((raw[1 + 2 * i], raw[2 + 2 * i]))
    return cases


# --- clause: build_row :: (k: int, n: int) -> list[int] ---
def build_row(k, n):
    row = [1]
    stride = 1
    while len(row) < k:
        nxt = row[-1] + stride
        first_side = k - len(row) - 1
        if nxt + first_side <= n:
            row.append(nxt)
            stride += 1
        else:
            row.append(row[-1] + 1)
    return row


# --- clause: main :: () -> None ---
def main():
    out = []
    for k, n in read_input():
        out.append(" ".join(map(str, build_row(k, n))))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
