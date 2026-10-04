import sys


# --- clause: read_input :: () -> tuple[list[int], list[int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    n = raw[0]
    return raw[1:1 + n], raw[1 + n:1 + 2 * n]


# --- clause: without_gap :: (row: list[int]) -> list[int] ---
def without_gap(row):
    return [number for number in row if number]


# --- clause: same_cycle :: (a: list[int], b: list[int]) -> bool ---
def same_cycle(a, b):
    if not a:
        return True
    if len(a) != len(b):
        return False
    begin = -1
    for i in range(0, len(b)):
        if b[i] == a[0]:
            begin = i
            break
    if begin < 0:
        return False
    for i in range(0, len(a)):
        if a[i] != b[(begin + i) % len(b)]:
            return False
    return True


# --- clause: main :: () -> None ---
def main():
    a, b = read_input()
    ok = same_cycle(without_gap(a), without_gap(b))
    sys.stdout.write("YES\n" if ok else "NO\n")


if __name__ == "__main__":
    main()
