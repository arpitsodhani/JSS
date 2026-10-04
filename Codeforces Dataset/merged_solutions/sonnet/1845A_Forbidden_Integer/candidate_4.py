import sys


# --- clause: read_input :: () -> list[tuple[int, int, int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    cases = []
    for i in range(t):
        cases.append((numbers[1 + 3 * i], numbers[2 + 3 * i], numbers[3 + 3 * i]))
    return cases


# --- clause: build_sum :: (n: int, k: int, x: int) -> list[int] | None ---
def build_sum(n, k, x):
    if x > 1:
        return [1] * n
    if k == 1:
        return None
    parts = []
    left = n
    if left % 2:
        if k < 3:
            return None
        parts.append(3)
        left -= 3
    while left:
        parts.append(2)
        left -= 2
    return parts if left == 0 else None


# --- clause: main :: () -> None ---
def main():
    pieces = []
    for n, k, x in read_input():
        parts = build_sum(n, k, x)
        if parts is None:
            pieces.append("NO")
        else:
            pieces.append("YES")
            pieces.append(str(len(parts)))
            pieces.append(" ".join(map(str, parts)))
    sys.stdout.write("\n".join(pieces) + "\n")


if __name__ == "__main__":
    main()
