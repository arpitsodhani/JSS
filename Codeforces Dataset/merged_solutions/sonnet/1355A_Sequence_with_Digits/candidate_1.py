import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    cases = []
    for i in range(t):
        cases.append((data[1 + 2 * i], data[2 + 2 * i]))
    return cases


# --- clause: run_sequence :: (start: int, k: int) -> int ---
def run_sequence(start, k):
    value = start
    for _ in range(k - 1):
        low = 9
        high = 0
        rest = value
        while rest:
            digit = rest % 10
            if digit < low:
                low = digit
            if digit > high:
                high = digit
            rest //= 10
        if low == 0:
            break
        value += low * high
    return value


# --- clause: main :: () -> None ---
def main():
    out = []
    for start, k in read_input():
        out.append(run_sequence(start, k))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
