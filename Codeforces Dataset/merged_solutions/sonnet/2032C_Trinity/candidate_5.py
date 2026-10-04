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


# --- clause: fewest_changes :: (a: list[int]) -> int ---
def fewest_changes(a):
    n = len(a)
    ranked = sorted(a)
    widest = 2
    low = 0
    for right in range(2, n):
        while ranked[low] + ranked[low + 1] <= ranked[right]:
            low += 1
        if right - low + 1 > widest:
            widest = right - low + 1
    return n - widest


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(fewest_changes(a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
