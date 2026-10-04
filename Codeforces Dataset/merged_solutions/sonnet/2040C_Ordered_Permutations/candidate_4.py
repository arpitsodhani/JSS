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


# --- clause: kth_permutation :: (n: int, k: int) -> list[int] | None ---
def kth_permutation(n, k):
    cap = 4 * 10 ** 12
    powers = [1] * (n + 1)
    for i in range(1, n + 1):
        powers[i] = powers[i - 1] * 2
        if powers[i] > cap:
            powers[i] = cap
    if powers[n - 1] < k:
        return None
    result = [0] * n
    low = 0
    high = n - 1
    left = k
    value = 1
    while low <= high:
        if low == high:
            result[low] = value
            break
        width = high - low + 1
        half = powers[width - 2]
        if left <= half:
            result[low] = value
            low += 1
        else:
            left -= half
            result[high] = value
            high -= 1
        value += 1
    return result

# --- clause: main :: () -> None ---
def main():
    out = []
    for n, k in read_input():
        order = kth_permutation(n, k)
        if order is None:
            out.append("-1")
        else:
            out.append(" ".join(map(str, order)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
