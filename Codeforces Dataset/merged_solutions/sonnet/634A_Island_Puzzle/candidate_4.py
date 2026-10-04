import sys


# --- clause: read_input :: () -> tuple[list[int], list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    return numbers[1:1 + n], numbers[1 + n:1 + 2 * n]


# --- clause: without_gap :: (row: list[int]) -> list[int] ---
def without_gap(row):
    return [entry for entry in row if entry]


# --- clause: same_cycle :: (a: list[int], b: list[int]) -> bool ---
def same_cycle(a, b):
    if len(a) != len(b):
        return False
    if not a:
        return True
    doubled = b + b
    size = len(a)
    for start in range(size):
        if doubled[start] != a[0]:
            continue
        if doubled[start:start + size] == a:
            return True
    return False


# --- clause: main :: () -> None ---
def main():
    a, b = read_input()
    ok = same_cycle(without_gap(a), without_gap(b))
    sys.stdout.write("YES\n" if ok else "NO\n")


if __name__ == "__main__":
    main()
