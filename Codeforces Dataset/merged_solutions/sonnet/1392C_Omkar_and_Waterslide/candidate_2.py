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


# --- clause: raise_count :: (a: list[int]) -> int ---
def raise_count(a):
    total = 0
    peak = a[0]
    for value in a[1:]:
        if value >= peak:
            peak = value
        else:
            total += peak - value
            peak = value
    return total


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(raise_count(a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
