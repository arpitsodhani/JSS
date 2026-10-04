import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    cases = []
    for i in range(t):
        cases.append((fields[1 + 2 * i], fields[2 + 2 * i]))
    return cases


# --- clause: build_row :: (k: int, n: int) -> list[int] ---
def build_row(k, n):
    row = [1]
    jump = 1
    while len(row) < k:
        nxt = row[-1] + jump
        begin = k - len(row) - 1
        if nxt + begin <= n:
            row.append(nxt)
            jump += 1
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
