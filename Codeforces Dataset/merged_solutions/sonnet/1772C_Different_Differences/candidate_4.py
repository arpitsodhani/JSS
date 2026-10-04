import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    cases = []
    for i in range(t):
        cases.append((numbers[1 + 2 * i], numbers[2 + 2 * i]))
    return cases


# --- clause: build_row :: (k: int, n: int) -> list[int] ---
def build_row(k, n):
    steps = 0
    while True:
        used = (steps + 1) * (steps + 2) // 2 + (k - 1 - (steps + 1))
        if steps + 1 <= k - 1 and used <= n - 1:
            steps += 1
        else:
            break
    row = [1]
    gap = 1
    for i in range(k - 1):
        if i < steps:
            row.append(row[-1] + gap)
            gap += 1
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
