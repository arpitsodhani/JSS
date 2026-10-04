import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    cases = []
    for i in range(t):
        cases.append((data[1 + 2 * i], data[2 + 2 * i]))
    return cases


# --- clause: build_row :: (k: int, n: int) -> list[int] ---
def build_row(k, n):
    row = [1]
    step = 1
    while len(row) < k:
        nxt = row[-1] + step
        left = k - len(row) - 1
        if nxt + left <= n:
            row.append(nxt)
            step += 1
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
