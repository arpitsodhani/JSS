import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    cases = []
    for i in range(t):
        cases.append((data[1 + 2 * i], data[2 + 2 * i]))
    return cases


# --- clause: best_total :: (n: int, m: int) -> int ---
def best_total(n, m):
    return (n if n > m else m) + 1


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, m in read_input():
        out.append(best_total(n, m))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
