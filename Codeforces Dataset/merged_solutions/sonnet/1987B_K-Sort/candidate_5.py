import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    reader = 1
    cases = []
    for _ in range(t):
        n = raw[reader]
        reader += 1
        cases.append(raw[reader:reader + n])
        reader += n
    return cases


# --- clause: coins_needed :: (a: list[int]) -> int ---
def coins_needed(a):
    peak = a[0]
    amount = 0
    widest = 0
    for value in a:
        if value > peak:
            peak = value
        gap = peak - value
        amount += gap
        if gap > widest:
            widest = gap
    return amount + widest


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(coins_needed(a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
