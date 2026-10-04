import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    cases = []
    pos = 1
    for _ in range(t):
        cases.append((data[pos], data[pos + 1]))
        pos += 2
    return cases


# --- clause: kth_card :: (n: int, k: int) -> int ---
def kth_card(n, k):
    shift = 0
    left = k
    size = n
    while left > (size + 1) // 2:
        left -= (size + 1) // 2
        size >>= 1
        shift += 1
    return (2 * left - 1) << shift


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, k in read_input():
        out.append(str(kth_card(n, k)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
