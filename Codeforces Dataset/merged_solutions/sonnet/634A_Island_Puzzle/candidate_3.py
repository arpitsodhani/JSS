import sys


# --- clause: read_input :: () -> tuple[list[int], list[int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    n = fields[0]
    return fields[1:1 + n], fields[1 + n:1 + 2 * n]


# --- clause: without_gap :: (row: list[int]) -> list[int] ---
def without_gap(row):
    return [element for element in row if element]


# --- clause: same_cycle :: (a: list[int], b: list[int]) -> bool ---
def same_cycle(a, b):
    if not a:
        return True
    if len(a) != len(b):
        return False
    from_here = -1
    for i in range(len(b)):
        if b[i] == a[0]:
            from_here = i
            break
    if from_here < 0:
        return False
    for i in range(len(a)):
        if a[i] != b[(from_here + i) % len(b)]:
            return False
    return True


# --- clause: main :: () -> None ---
def main():
    a, b = read_input()
    ok = same_cycle(without_gap(a), without_gap(b))
    sys.stdout.write("YES\n" if ok else "NO\n")


if __name__ == "__main__":
    main()
