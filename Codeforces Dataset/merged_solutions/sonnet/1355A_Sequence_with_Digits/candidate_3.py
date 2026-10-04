import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    cases = []
    for i in range(t):
        cases.append((fields[1 + 2 * i], fields[2 + 2 * i]))
    return cases


# --- clause: run_sequence :: (start: int, k: int) -> int ---
def run_sequence(start, k):
    entry = start
    for _ in range(k - 1):
        low = 9
        upper = 0
        rest = entry
        while rest:
            digit = rest % 10
            if digit < low:
                low = digit
            if digit > upper:
                upper = digit
            rest //= 10
        if low == 0:
            break
        entry += low * upper
    return entry


# --- clause: main :: () -> None ---
def main():
    out = []
    for start, k in read_input():
        out.append(run_sequence(start, k))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
