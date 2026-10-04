import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        cases.append((data[pos], data[pos + 1], data[pos + 2], data[pos + 3]))
        pos += 4
    return cases


# --- clause: kth_equality :: (a_len: int, b_len: int, c_len: int, k: int) -> str ---
def kth_equality(a_len, b_len, c_len, k):
    low_a = 10 ** (a_len - 1)
    high_a = 10 ** a_len - 1
    low_b = 10 ** (b_len - 1)
    high_b = 10 ** b_len - 1
    low_c = 10 ** (c_len - 1)
    high_c = 10 ** c_len - 1
    remaining = k
    for a in range(low_a, high_a + 1):
        first = low_c - a
        if first < low_b:
            first = low_b
        last = high_c - a
        if last > high_b:
            last = high_b
        if last < first:
            continue
        span = last - first + 1
        if remaining > span:
            remaining -= span
            continue
        b = first + remaining - 1
        return "%d + %d = %d" % (a, b, a + b)
    return "-1"


# --- clause: main :: () -> None ---
def main():
    out = []
    for a_len, b_len, c_len, k in read_input():
        out.append(kth_equality(a_len, b_len, c_len, k))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
