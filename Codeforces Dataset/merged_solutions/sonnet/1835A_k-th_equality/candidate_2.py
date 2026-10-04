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
    start_a = 10 ** (a_len - 1)
    stop_a = 10 ** a_len
    start_b = 10 ** (b_len - 1)
    stop_b = 10 ** b_len
    start_c = 10 ** (c_len - 1)
    stop_c = 10 ** c_len
    left = k
    for a in range(start_a, stop_a):
        lo = max(start_b, start_c - a)
        hi = min(stop_b - 1, stop_c - 1 - a)
        count = hi - lo + 1
        if count <= 0:
            continue
        if left <= count:
            b = lo + left - 1
            return str(a) + " + " + str(b) + " = " + str(a + b)
        left -= count
    return "-1"


# --- clause: main :: () -> None ---
def main():
    out = []
    for a_len, b_len, c_len, k in read_input():
        out.append(kth_equality(a_len, b_len, c_len, k))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
