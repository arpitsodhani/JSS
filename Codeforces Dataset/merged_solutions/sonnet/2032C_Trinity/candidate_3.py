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


# --- clause: fewest_changes :: (a: list[int]) -> int ---
def fewest_changes(a):
    n = len(a)
    ranked = sorted(a)
    widest = 2
    start = 0
    for right in range(2, n):
        while ranked[start] + ranked[start + 1] <= ranked[right]:
            start += 1
        if right - start + 1 > widest:
            widest = right - start + 1
    return n - widest


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(fewest_changes(a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
