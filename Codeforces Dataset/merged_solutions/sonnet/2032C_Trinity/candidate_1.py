import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        cases.append(data[pos:pos + n])
        pos += n
    return cases


# --- clause: fewest_changes :: (a: list[int]) -> int ---
def fewest_changes(a):
    n = len(a)
    ranked = sorted(a)
    widest = 2
    left = 0
    for right in range(2, n):
        while ranked[left] + ranked[left + 1] <= ranked[right]:
            left += 1
        if right - left + 1 > widest:
            widest = right - left + 1
    return n - widest


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(fewest_changes(a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
