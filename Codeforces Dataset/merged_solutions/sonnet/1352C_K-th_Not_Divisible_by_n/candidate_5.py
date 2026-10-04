import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    cases = []
    pos = 1
    for _ in range(t):
        cases.append((int(data[pos]), int(data[pos + 1])))
        pos += 2
    return cases


# --- clause: kth_free :: (n: int, k: int) -> int ---
def kth_free(n, k):
    lo = 1
    hi = 2 * k + 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if mid - mid // n < k:
            lo = mid + 1
        else:
            hi = mid
    return lo


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, k in read_input():
        out.append(str(kth_free(n, k)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
