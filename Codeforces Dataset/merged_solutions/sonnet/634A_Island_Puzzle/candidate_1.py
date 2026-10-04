import sys


# --- clause: read_input :: () -> tuple[list[int], list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    return data[1:1 + n], data[1 + n:1 + 2 * n]


# --- clause: without_gap :: (row: list[int]) -> list[int] ---
def without_gap(row):
    return [value for value in row if value]


# --- clause: same_cycle :: (a: list[int], b: list[int]) -> bool ---
def same_cycle(a, b):
    if not a:
        return True
    if len(a) != len(b):
        return False
    start = -1
    for i in range(len(b)):
        if b[i] == a[0]:
            start = i
            break
    if start < 0:
        return False
    for i in range(len(a)):
        if a[i] != b[(start + i) % len(b)]:
            return False
    return True


# --- clause: main :: () -> None ---
def main():
    a, b = read_input()
    ok = same_cycle(without_gap(a), without_gap(b))
    sys.stdout.write("YES\n" if ok else "NO\n")


if __name__ == "__main__":
    main()
