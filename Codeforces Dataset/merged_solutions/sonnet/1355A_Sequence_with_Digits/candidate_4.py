import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    cases = []
    for i in range(t):
        cases.append((numbers[1 + 2 * i], numbers[2 + 2 * i]))
    return cases


# --- clause: run_sequence :: (start: int, k: int) -> int ---
def run_sequence(start, k):
    value = start
    steps = k - 1
    while steps > 0:
        digits = [int(ch) for ch in str(value)]
        low = min(digits)
        if low == 0:
            break
        value += low * max(digits)
        steps -= 1
    return value


# --- clause: main :: () -> None ---
def main():
    out = []
    for start, k in read_input():
        out.append(run_sequence(start, k))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
