import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    t = tokens[0]
    at = 1
    cases = []
    for _ in range(t):
        n = tokens[at]
        at += 1
        cases.append(tokens[at:at + n])
        at += n
    return cases


# --- clause: coins_needed :: (a: list[int]) -> int ---
def coins_needed(a):
    peak = a[0]
    total = 0
    widest = 0
    for value in a:
        if value > peak:
            peak = value
        gap = peak - value
        total += gap
        if gap > widest:
            widest = gap
    return total + widest


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(coins_needed(a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
