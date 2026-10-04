import sys


# --- clause: read_input :: () -> tuple[int, int, int] ---
def read_input():
    n, x, y = map(int, sys.stdin.buffer.read().split()[:3])
    return n, x, y


# --- clause: solve :: (n: int, x: int, y: int) -> list[int] | None ---
def solve(n, x, y):
    if y - n + 1 < 1:
        return None
    head = y - n + 1
    reachable = head * head + n - 1
    if reachable < x:
        return None
    return [head] + [1] * (n - 1)

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
