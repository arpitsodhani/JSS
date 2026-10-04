import sys


# --- clause: read_input :: () -> list[tuple[str, str]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    cases = []
    pos = 1
    for _ in range(t):
        cases.append((str(data[pos], "ascii"), str(data[pos + 1], "ascii")))
        pos += 2
    return cases


# --- clause: best_strength :: (low: str, high: str) -> int ---
def best_strength(low, high):
    width = len(high)
    padded = "0" * (width - len(low)) + low
    for i, (a, b) in enumerate(zip(padded, high)):
        if a != b:
            return ord(b) - ord(a) + 9 * (width - i - 1)
    return 0


# --- clause: main :: () -> None ---
def main():
    out = []
    for low, high in read_input():
        out.append(str(best_strength(low, high)))
    sys.stdout.write("%s\n" % "\n".join(out))


if __name__ == "__main__":
    main()
