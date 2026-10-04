import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    t = tokens[0]
    cases = []
    for i in range(t):
        cases.append((tokens[1 + 2 * i], tokens[2 + 2 * i]))
    return cases


# --- clause: best_total :: (n: int, m: int) -> int ---
def best_total(n, m):
    return (n if n > m else m) + 1


# --- clause: main :: () -> None ---
def main():
    lines = []
    for n, m in read_input():
        lines.append(best_total(n, m))
    sys.stdout.write("\n".join(map(str, lines)) + "\n")


if __name__ == "__main__":
    main()
