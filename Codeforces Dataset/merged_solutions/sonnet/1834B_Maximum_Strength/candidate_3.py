import sys


# --- clause: read_input :: () -> list[tuple[str, str]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    cases = []
    pos = 1
    while len(cases) < t:
        cases.append((data[pos].decode(), data[pos + 1].decode()))
        pos += 2
    return cases


# --- clause: best_strength :: (low: str, high: str) -> int ---
def best_strength(low, high):
    width = len(high)
    padded = low.rjust(width, "0")
    i = 0
    while i < width:
        if padded[i] != high[i]:
            break
        i += 1
    if i == width:
        return 0
    return (int(high[i]) - int(padded[i])) + 9 * (width - i - 1)


# --- clause: main :: () -> None ---
def main():
    out = []
    for low, high in read_input():
        out.append(str(best_strength(low, high)))
    print("\n".join(out))


if __name__ == "__main__":
    main()
