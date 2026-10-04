import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    offset = 1
    cases = []
    for _ in range(t):
        n = fields[offset]
        offset += 1
        cases.append(fields[offset:offset + n])
        offset += n
    return cases


# --- clause: coins_needed :: (a: list[int]) -> int ---
def coins_needed(a):
    peak = a[0]
    summed = 0
    widest = 0
    for value in a:
        if value > peak:
            peak = value
        gap = peak - value
        summed += gap
        if gap > widest:
            widest = gap
    return summed + widest


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(coins_needed(a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
