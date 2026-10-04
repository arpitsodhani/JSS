import sys


# --- clause: read_input :: () -> list[tuple[str, str]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    cases = []
    pos = 1
    for _ in range(t):
        low = data[pos].decode()
        pos += 1
        high = data[pos].decode()
        pos += 1
        cases.append((low, high))
    return cases


# --- clause: best_strength :: (low: str, high: str) -> int ---
def best_strength(low, high):
    width = len(high)
    padded = low.zfill(width)
    for i in range(width):
        if padded[i] != high[i]:
            return (int(high[i]) - int(padded[i])) + 9 * (width - i - 1)
    return 0


# --- clause: main :: () -> None ---
def main():
    out = []
    for low, high in read_input():
        out.append(str(best_strength(low, high)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
