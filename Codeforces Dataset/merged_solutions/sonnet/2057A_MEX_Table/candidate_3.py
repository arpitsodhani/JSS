import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    cases = []
    for i in range(t):
        cases.append((fields[1 + 2 * i], fields[2 + 2 * i]))
    return cases


# --- clause: best_total :: (n: int, m: int) -> int ---
def best_total(n, m):
    return (n if n > m else m) + 1


# --- clause: main :: () -> None ---
def main():
    collected = []
    for n, m in read_input():
        collected.append(best_total(n, m))
    sys.stdout.write("\n".join(map(str, collected)) + "\n")


if __name__ == "__main__":
    main()
