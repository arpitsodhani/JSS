import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    cases = []
    for i in range(t):
        cases.append((numbers[1 + 2 * i], numbers[2 + 2 * i]))
    return cases


# --- clause: best_total :: (n: int, m: int) -> int ---
def best_total(n, m):
    wide = [n, m]
    wide.sort()
    return wide[1] + 1


# --- clause: main :: () -> None ---
def main():
    pieces = []
    for n, m in read_input():
        pieces.append(best_total(n, m))
    sys.stdout.write("\n".join(map(str, pieces)) + "\n")


if __name__ == "__main__":
    main()
