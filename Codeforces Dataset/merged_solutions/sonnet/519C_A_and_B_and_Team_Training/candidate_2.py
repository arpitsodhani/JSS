import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    n, m = map(int, sys.stdin.buffer.read().split())
    return n, m


# --- clause: compute_answer :: (n: int, m: int) -> int ---
def compute_answer(n, m):
    teams = (n + m) // 3
    return min(min(n, m), teams)


# --- clause: main :: () -> None ---
def main():
    n, m = read_input()
    sys.stdout.write(str(compute_answer(n, m)) + "\n")


if __name__ == "__main__":
    main()
