import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[0], numbers[1]


# --- clause: build_sequence :: (n: int, k: int) -> str | None ---
def build_sequence(n, k):
    if k > n * (n - 1) // 2:
        return None
    row = []
    depth = 0
    left = k
    opened = 0
    for _ in range(n):
        if left >= depth:
            left -= depth
            row.append("(")
            depth += 1
            opened += 1
        else:
            while depth > left:
                row.append(")")
                depth -= 1
            left -= depth
            row.append("(")
            depth += 1
            opened += 1
    while depth:
        row.append(")")
        depth -= 1
    return "".join(row)


# --- clause: main :: () -> None ---
def main():
    n, k = read_input()
    answer = build_sequence(n, k)
    sys.stdout.write("Impossible\n" if answer is None else answer + "\n")


if __name__ == "__main__":
    main()
