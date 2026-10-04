import sys


# --- clause: read_input :: () -> list[tuple[str, str]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    cases = []
    for i in range(t):
        cases.append((data[2 * i + 1].decode(), data[2 * i + 2].decode()))
    return cases


# --- clause: best_strength :: (low: str, high: str) -> int ---
def best_strength(low, high):
    width = len(high)
    padded = low.rjust(width, "0")
    for i in range(width):
        if padded[i] != high[i]:
            return (int(high[i]) - int(padded[i])) + 9 * (width - i - 1)
    return 0


# --- clause: main :: () -> None ---
def main():
    out = []
    for case in read_input():
        out.append(str(best_strength(case[0], case[1])))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
