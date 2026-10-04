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
    lines = []
    for a in read_input():
        lines.append("YES" if is_bitonic(a) else "NO")
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
