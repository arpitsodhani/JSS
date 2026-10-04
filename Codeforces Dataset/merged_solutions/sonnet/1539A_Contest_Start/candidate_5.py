import sys


# --- clause: read_input :: () -> list[tuple[int, int, int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    k = data[0]
    cases = []
    pos = 1
    for _ in range(k):
        cases.append((data[pos], data[pos + 1], data[pos + 2]))
        pos += 3
    return cases


# --- clause: total_dissatisfaction :: (n: int, x: int, t: int) -> int ---
def total_dissatisfaction(n, x, t):
    reach = t // x
    if reach >= n:
        return n * (n - 1) // 2
    return (n - reach) * reach + reach * (reach - 1) // 2



# --- clause: main :: () -> None ---
def main():
    out = []
    for n, x, t in read_input():
        out.append(str(total_dissatisfaction(n, x, t)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
