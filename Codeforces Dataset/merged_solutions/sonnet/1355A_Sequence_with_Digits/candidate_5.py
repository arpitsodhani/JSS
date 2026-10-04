import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    cases = []
    for i in range(t):
        cases.append((raw[1 + 2 * i], raw[2 + 2 * i]))
    return cases


# --- clause: run_sequence :: (start: int, k: int) -> int ---
def run_sequence(start, k):
    item = start
    for _ in range(k - 1):
        low = 9
        ceiling_value = 0
        rest = item
        while rest:
            digit = rest % 10
            if digit < low:
                low = digit
            if digit > ceiling_value:
                ceiling_value = digit
            rest //= 10
        if low == 0:
            break
        item += low * ceiling_value
    return item


# --- clause: main :: () -> None ---
def main():
    out = []
    for start, k in read_input():
        out.append(run_sequence(start, k))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
