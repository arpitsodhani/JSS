import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    t = tokens[0]
    cases = []
    for i in range(t):
        cases.append((tokens[1 + 2 * i], tokens[2 + 2 * i]))
    return cases


# --- clause: run_sequence :: (start: int, k: int) -> int ---
def run_sequence(start, k):
    value = start
    for _ in range(k - 1):
        low = 9
        top_value = 0
        rest = value
        while rest:
            digit = rest % 10
            if digit < low:
                low = digit
            if digit > top_value:
                top_value = digit
            rest //= 10
        if low == 0:
            break
        value += low * top_value
    return value


# --- clause: main :: () -> None ---
def main():
    out = []
    for start, k in read_input():
        out.append(run_sequence(start, k))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
