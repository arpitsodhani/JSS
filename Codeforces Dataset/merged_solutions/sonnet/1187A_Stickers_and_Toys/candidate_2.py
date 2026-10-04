import sys


# --- clause: read_input :: () -> list[tuple[int, int, int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    cases = []
    pos = 1
    for _ in range(t):
        cases.append((data[pos], data[pos + 1], data[pos + 2]))
        pos += 3
    return cases


# --- clause: eggs_needed :: (n: int, s: int, t: int) -> int ---
def eggs_needed(n, s, t):
    return max(n - s, n - t) + 1


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, s, t in read_input():
        out.append(str(eggs_needed(n, s, t)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
