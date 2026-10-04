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


# --- clause: is_bitonic :: (a: list[int]) -> bool ---
def is_bitonic(a):
    i = 0
    n = len(a)
    while i + 1 < n and a[i] <= a[i + 1]:
        i += 1
    while i + 1 < n and a[i] >= a[i + 1]:
        i += 1
    return i == n - 1


# --- clause: main :: () -> None ---
def main():
    pieces = []
    for a in read_input():
        pieces.append("YES" if is_bitonic(a) else "NO")
    sys.stdout.write("\n".join(pieces) + "\n")


if __name__ == "__main__":
    main()
