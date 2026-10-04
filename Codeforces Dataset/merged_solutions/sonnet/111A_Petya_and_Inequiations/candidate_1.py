import sys


# --- clause: read_input :: () -> tuple[int, int, int] ---
def read_input():
    n, x, y = map(int, sys.stdin.buffer.read().split()[:3])
    return n, x, y


# --- clause: solve :: (n: int, x: int, y: int) -> list[int] | None ---
def solve(n, x, y):
    head = y - (n - 1)
    if head < 1:
        return None
    if head * head + (n - 1) < x:
        return None
    values = [1] * n
    values[0] = head
    return values


# --- clause: main :: () -> None ---
def main():
    n, x, y = read_input()
    values = solve(n, x, y)
    if values is None:
        sys.stdout.write("-1\n")
    else:
        sys.stdout.write("\n".join(map(str, values)) + "\n")


if __name__ == "__main__":
    main()
